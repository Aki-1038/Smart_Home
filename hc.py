import cv2
import torch
from ultralytics import YOLO
import numpy as np
from flask import Flask, render_template, Response, jsonify
import threading

app = Flask(__name__)

# 全域變數
current_person_count = 0
frame_buffer = None
frame_lock = threading.Lock()

# 載入YOLO模型
try:
    model = YOLO('yolov8n.pt')
except Exception as e:
    print(f"模型載入失敗: {e}")
    exit()


def generate_frames():
    global frame_buffer
    while True:
        with frame_lock:
            if frame_buffer is not None:
                ret, buffer = cv2.imencode('.jpg', frame_buffer)
                if not ret:
                    continue
                frame_bytes = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


def detect_people():
    global current_person_count, frame_buffer
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("無法開啟攝影機")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        person_count = 0

        for r in results:
            boxes = r.boxes
            for box in boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])

                if cls == 0 and conf > 0.5:  # 人類類別且信心度>0.5
                    person_count += 1
                    x1, y1, x2, y2 = box.xyxy[0]
                    cv2.rectangle(frame,
                                  (int(x1), int(y1)),
                                  (int(x2), int(y2)),
                                  (0, 255, 0), 2)

        current_person_count = person_count

        # 根據人數選擇顏色
        text_color = (0, 255, 0) if person_count == 0 else (0, 0, 255)

        # 使用 putText 顯示中文
        cv2.putText(frame, f'目前人數: {person_count} 人',
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1, text_color, 2)

        # 更新 frame_buffer
        with frame_lock:
            frame_buffer = frame.copy()


@app.route('/')
def index():
    return render_template('hc.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/get_count')
def get_count():
    return jsonify({'count': current_person_count})


if __name__ == '__main__':
    # 啟動偵測執行緒
    detection_thread = threading.Thread(target=detect_people)
    detection_thread.daemon = True
    detection_thread.start()

    # 啟動 Flask 伺服器
    app.run(debug=False, port=5001, host='0.0.0.0')
