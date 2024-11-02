資訊管理實務專題製作 
===
## 主題：智慧家庭

---

## 工作日誌
<style>
.blue {color: blue;}
</style>

| 日期  | 主題 | 內容 |   備註|
| --- | ----- | ----- | ------------------------------  |
| 2024/09/16 | 購買參考書       |快速學會Python架站技術:活用Django 4 建構動態網站的16堂課 | |
| 2024/09/17 | 專題題目 |設定專題題目智慧家庭相關  | |
| 2024/09/17 | ESP32選型及規格比較       |NodeMCU-32S | |
| 2024/09/25 | 購買參考書       |ESP32物聯網基礎10門課 | |
| 2024/10/01 | 購買ESP32  |  型號：NodeMCU-32 |https://www.taiwaniot.com.tw/product/nodemcu-32s%E6%93%B4%E5%B1%95%E6%9D%BF-esp32-lua-wifi-%E6%93%B4%E5%B1%95%E6%9D%BF-%E6%94%AF%E6%8F%B4dc%E9%9B%BB%E6%BA%90%E4%BE%9B%E9%9B%BB/|
| 2024/10/02 | 購買參考書       |Django 5企業級Web應用開發實戰（視頻教學版） | |
| 2024/10/07 |申請Github Copilot       | | |
| 2024/10/07 |論文整理            |上傳論文至NotebookLM，整理論文筆記 |  |
| 2024/10/08 |  arduino       |開發程式下載、安裝、開發環境學習 | |
| 2024/10/08 | IO 測試           | <span class="blue">Blinking an LED With ESP32</span>|
| 2024/10/08 |   wifi連線測試     |打開序列埠監控視窗：觀察ESP32所分配到的IP位址以及WiFi強度。 | |
| 2024/10/08 | NTPClient       |連接到時間伺服器的 NTPClient 從 NTP 伺服器取得時間並保持同步。 | |
| 2024/10/08 | MySQL_Connector_Arduino       |將 Arduino 專案直接連接到 MySQL 伺服器 | |
| 2024/10/17 |test_mysql.py        |測試mysql 連線 | |
| 2024/10/ |        | | |
| 2024/10/ |        | | |
	
---

專題製作期初提案報告
===

### 1. 專題背景與動機

#### a. 智慧家庭的發展
隨著物聯網 (IoT) 技術的發展，智慧家庭逐漸進入主流市場。智慧家庭系統可以自動化控制家庭中的設備，提升生活便利性和節能效益。但許多商業系統昂貴且不具彈性，因此藉由這個課程開發一個基於開源硬體和軟體的低成本之智慧家庭系統。

---

#### b. 問題陳述
在7年前搬到目前居住的家時，就規劃並實現一套智慧家庭系統，目前使用智慧家庭方案有Apple、LG及米家的生態系產品，控制的對象包括影音系統、電燈、掃地機器人、電扇、空氣清淨機、冰箱、洗衣機及加壓馬達...等，環境感測器包括溫度、濕度、PM2.5、漏水感測器、人體感測器、門窗感測器及監視器...等。雖然使用上確實為生活帶來安仼感及很多的便利，但還是有些地方需要再加強。
1. 空調系統：在空調方面，當時選擇的是日本壓縮機很稀少而且很貴的品牌，因為當時是少數具備可以連線網路的機種。但安裝後發現不能連線；原廠表示控制模組要另外購買且缺貨要等三個月至半年，待有貨時再通知，沒想到一年後還是沒貨，而且價格不便宜。因此，空調這個部份就成了這個系統的一個缺口。
2. 供水系統：水塔水位偵測防止供水系統故障無水可用的問題發生。
3. 改善室內空氣品質：空氣清淨機難以在短時間將烹調食物後所產生的空氣污染消除，控制排油煙機自動開機及關機。

市售智慧家庭系統的設置功能較簡單，難以擴展和自定義功能。而使用 NodeMCU-32S 等開發板的物聯網系統，具有靈活、易於擴展且成本低廉的優點。

---

### 2. 研究目標

專題的目標是在家庭中設置一個基於 NodeMCU-32S 的智慧家庭系統，並在 Synology NAS 建立一個控制網站，使家庭中的各種感測器和設備能夠遠端監視及控制。具體功能包括：

1. 頂樓水塔液位偵測及警報
2. 廚房 PM2.5 偵測與排油煙機自動控制
3. 各房間溫度偵測及冷氣遠端控制
4. 前院人體移動偵測與攝影機監控
這些功能將實現智慧家庭中環境監控、家電控制及安全防護功能的整合。

---

### 3. 研究範圍與方法

#### a. 硬體架構
每個功能模組將使用 NodeMCU-32S 作為核心控制單元，搭配相應的感測器及控制器，具體包括：
- 水塔液位感測器
- PM2.5 感測器與繼電器
- 溫度感測器與紅外線發射器
- 微波雷達感測模組與攝影機模組

---

#### b. 軟體架構
- 使用 Arduino IDE 來開發 NodeMCU-32S 的控制程式。
- 開發網頁介面，透過 Wi-Fi 連接 NodeMCU-32S 與 NAS web server，實現資料的儲存與操作。
- 使用 LINEBOT 來通知使用者異常狀況，如液位過低或 PM2.5 數值超標。

---

#### c. 網路通訊
NodeMCU-32S 會定期將感測數據上傳至 NAS 伺服器，並透過 HTTP 網頁進行資料交換。

---

### 4. 預期成果 (Expected Outcomes)

專題完成後，系統將具備以下功能：
1. 頂樓水塔液位偵測與即時通知
2. 廚房 PM2.5 檢測與自動抽油煙機控制
3. 房間溫度偵測與冷氣遠端控制
4. 前院人體移動偵測與視頻監控

此外，使用者可以透過網頁介面進行操作，系統具備即時反饋功能，並將數據安全儲存在家庭 NAS 上。

---

### 5. 計畫進度 (Project Timeline)

- **第一階段**：系統架構設計與硬體選型
- **第二階段**：硬體組裝與程式開發
- **第三階段**：後端與前端開發
- **第四階段**：整合測試與錯誤排查
- **第五階段**：期末展示與報告撰寫

---

專題執行內容
===

### 硬體規劃

---

| No.| 	ESP模組| 	位置	| 功能描述| 	輸入信號| 	輸出信號| 	說明	| IP address| 
| --- | ----- | ----- |	 ----- |	 ----- |	 ----- |	 ----- |	 ----- 	| 
| 1	| NodeMCU-32S	| 頂樓	| 頂樓水塔液位偵測	| 液位感測器 * 1個| | 當水塔的水位太低，液位計輸出信號為LOW, NodeMCU-32S透過LINEBOT通知使用者，收到通知後透過aki920p.myDS.me的專題製作網頁檢視信號的狀態	| 192.168.68.116| 
| 2	| NodeMCU-32S| 	1樓| 	1樓廚房PM2.5偵測及抽油煙機開關控制| 	PM2.5感測器* 1個| 	繼電器 * 3個| 	當感測器偵測到空氣品質PM2.5 數值 > 10時，3個繼電器每隔1秒依序起動使接點導通讓排油煙機啟動，將室內的空氣排到戶戶外, NodeMCU-32S透過LINEBOT通知使用者，收到通知後透過aki920p.myDS.me的專題製作網頁檢視信號的狀態	| 192.168.68.117| 
| 3	| NodeMCU-32S| 	1樓| 	1樓客廳溫度偵測及冷氣開關機控制| 	溫度感測器 * 1個| 	紅外線發射器 * 1個| 	功能1：使用者可設定時間，當定時器功能啟動狀態時，讀取溫度感測器溫度，若室內溫度高於28℃時，紅外線發射器輸出啟動冷氣電源的搖控器編碼，打開冷氣。 功能2：使用者可透過網頁的開/關控制按鈕遠端控制冷氣 | 	192.168.68.118 | 
| 4	| NodeMCU-32S| 	2樓前| 	2樓前房闁溫度偵測及冷氣開關機控制| 	溫度感測器 * 1個| 	紅外線發射器 * 1個 | 	功能1：使用者可設定時間，當定時器功能啟動狀態時，讀取溫度感測器溫度，若室內溫度高於28℃時，紅外線發射器輸出啟動冷氣電源的搖控器編碼，打開冷氣。功能2：使用者可透過網頁的開/關控制按鈕遠端控制冷氣| 	192.168.68.119 | 
| 5	| NodeMCU-32S	| 2樓後| 	2樓後房闁溫度偵測及冷氣開關機控制| 	溫度感測器 * 1個| 	紅外線發射器 * 1個	| 功能1：使用者可設定時間，當定時器功能啟動狀態時，讀取溫度感測器溫度，若室內溫度高於28℃時，紅外線發射器輸出啟動冷氣電源的搖控器編碼，打開冷氣。功能2：使用者可透過網頁的開/關控制按鈕遠端控制冷氣| 	192.168.68.120| 
| 6	| NodeMCU-32S	| 3樓前| 	3樓前房闁溫度偵測及冷氣開關機控制| 	溫度感測器 * 1個	| 紅外線發射器 * 1個	| 功能1：使用者可設定時間，當定時器功能啟動狀態時，讀取溫度感測器溫度，若室內溫度高於28℃時，紅外線發射器輸出啟動冷氣電源的搖控器編碼，打開冷氣。功能2：使用者可透過網頁的開/關控制按鈕遠端控制冷氣| 	192.168.68.121| 
| 7	| NodeMCU-32S	| 3樓後| 	3樓後房闁溫度偵測及冷氣開關機控制| 	溫度感測器 * 1個	| 紅外線發射器 * 1個	| 功能1：使用者可設定時間，當定時器功能啟動狀態時，讀取溫度感測器溫度，若室內溫度高於28℃時，紅外線發射器輸出啟動冷氣電源的搖控器編碼，打開冷氣。功能2：使用者可透過網頁的開/關控制按鈕遠端控制冷氣| 	192.168.68.122| 
| 8	| NodeMCU-33S	| 前院	| 前院物體移動感測及攝影機監視| 	RCWL-0516 微波雷達人体感測模組 * 1個，紅外線人體感測器 * 1個|  OV2640攝影機模組 * 1	| 當感測器偵測到前院有人員移動時，模組輸出信號為HIGH, NodeMCU-32S透過LINEBOT通知使用者，收到通知後透過aki920p.myDS.me的專題製作網頁檢視信號的狀態	| 192.168.68.123| 

---

### 人機介面
#### 登入系統驗證：
登入：輸入帳號及密碼

---

#### 系統操控介面：
- 樓層：
一樓, 二樓, 三樓, 四樓, 頂樓

- 監控對象：
冷氣：一樓, 二樓前, 二樓後,  三樓前, 三樓後
水塔：一樓, 頂樓
馬達：一樓抽馬達, 頂樓加壓馬達
照明：照明總開關
環境：一樓溫度, 一樓濕度

---

IoT
===
## ESP32 各主要版本的比較表：
以下是 ESP32 各主要版本的比較表：

| 版本名稱      | 主要特性                           | CPU 核心   | 記憶體 (RAM) | Wi-Fi 支援 | 藍牙支援 | 應用範圍                              |
|---------------|------------------------------------|------------|--------------|------------|----------|----------------------------------------|
| **ESP32-WROOM** | 基本模組，性價比高                 | 2 核心 Xtensa | 520 KB       | 802.11 b/g/n | BT/BLE 4.2 | 一般 IoT 應用，如智能家居              |
| **ESP32-WROVER** | 增加 PSRAM，適合影像處理等應用    | 2 核心 Xtensa | 4MB PSRAM    | 802.11 b/g/n | BT/BLE 4.2 | 需要大量記憶體的應用，如影像、音訊處理 |
| **ESP32-S2**    | 單核心，降低功耗                  | 1 核心 Xtensa | 320 KB       | 802.11 b/g/n | 不支援藍牙 | 安全 IoT 應用，降低功耗                |
| **ESP32-C3**    | RISC-V 架構，性價比高，安全性增強 | 1 核心 RISC-V | 400 KB       | 802.11 b/g/n | BT/BLE 5.0 | IoT 設備，適合無需高性能的應用          |
| **ESP32-S3**    | 增加向量處理，適合 AIoT 應用     | 2 核心 Xtensa | 512 KB       | 802.11 b/g/n | BT/BLE 5.0 | AIoT、影像識別等應用                   |

這些版本各自針對不同應用場景設計，從基本的 IoT 應用到需要高記憶體、AI 或安全需求的情境。

---
python 程式
===
### mysql測試：
#### 由database "food" 下SELECT * FROM users指令
```
import mysql.connector
from mysql.connector import Error

# MySQL 伺服器連接設置
# host = '127.0.0.1'
# host = '172.20.10.5'
host = '116.118.152.93'
port = 3306
user = 'aki'
password = 'Md-3308333'
database = 'food'

try:
    # 建立與 MySQL 的連接
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print(f"Connected to MySQL server on {host}")

        # 創建游標
        cursor = connection.cursor()

        # 執行 SQL 查詢以獲取 users 表的內容
        cursor.execute("SELECT * FROM users")

        # 獲取查詢結果
        rows = cursor.fetchall()

        # 顯示查詢結果
        print(f"Total rows in 'users' table: {cursor.rowcount}")
        for row in rows:
            print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
                

```
---
#### 連線成功傳回：
```
Connected to MySQL server on 116.118.152.93
Total rows in 'users' table: 36
(1, 'wane1028', '1028', '林文祥', None, None, None, None, None, '管理者', None, None, None)
(2, 'wane', '1028', '林文祥', None, None, None, None, None, '老師', None, None, None)
(4, '13007003', '13007003', '王麗秋', None, None, '', None, '13', '學生', None, None, None)
(5, '13007004', '13007004', '吳貞慧', None, None, '', None, '13', '學生', None, None, None)
(6, '13007008', '13007008', '李育瑜', None, None, None, None, None, '學生', None, None, None)
(7, '13007009', '13007009', '李欣如', None, None, None, None, None, '學生', None, None, None)
(8, '13007013', '13007013', '林莉娟', None, None, None, None, None, '學生', None, None, None)
(9, '13007019', '13007019', '莊雅筑', None, None, None, None, None, '學生', None, None, None)
(10, '13007020', '13007020', '許卉玟', None, None, None, None, None, '學生', None, None, None)
(11, '13007022', '13007022', '郭亭君', None, None, None, None, None, '學生', None, None, None)
(12, '13007024', '13007024', '陳慧宣', None, None, None, None, None, '學生', None, None, None)
(13, '13007026', '13007026', '曾郁祺', None, None, None, None, None, '學生', None, None, None)
(14, '13007027', '13007027', '游婷如', None, None, None, None, None, '學生', None, None, None)
(15, '13007032', '13007032', '溫佳貞', None, None, None, None, '', '管理者', '', '', None)
(16, '13007033', '13007033', '廖君霈', None, None, None, None, '', '管理者', '', '', None)
(17, '13007034', '13007034', '蔡桂琳', None, None, None, None, None, '學生', None, None, None)
(18, '13007036', '13007036', '謝宜珊', None, None, None, None, None, '學生', None, None, None)
(19, '13007043', '13007043', '陳駿逸', None, None, None, None, None, '學生', None, None, None)
(20, '13007044', '13007044', '黃裕楷', None, None, None, None, None, '學生', None, None, None)
(21, '13007045', '13007045', '楊成富', None, None, None, None, None, '學生', None, None, None)
(22, '13007047', '13007047', '韓洸毅', None, None, None, None, None, '學生', None, None, None)
(23, '13007006', '13007006', '李伊翔', None, None, '', None, '13', '學生', None, None, None)
(24, '13007007', '13007007', '李沂真', None, None, None, None, None, '學生', None, None, None)
(25, '13007011', '13007011', '林吟芳', None, None, None, None, '', '管理者', '', '', None)
(26, '13007014', '13007014', '林曉君', None, None, None, None, None, '學生', None, None, None)
(27, '13007015', '13007015', '施育雯', None, None, None, None, '', '管理者', '', '', None)
(28, '13007016', '13007016', '張芝瑋', None, None, None, None, None, '學生', None, None, None)
(29, '13007017', '13007017', '張書瑜', None, None, None, None, None, '學生', None, None, None)
(30, '13007023', '13007023', '陳威樺', None, None, None, None, None, '學生', None, None, None)
(31, '13007025', '13007025', '傅彥慈', None, None, None, None, None, '學生', None, None, None)
(32, '13007031', '13007031', '楊\u3000翎', None, None, None, None, None, '學生', None, None, None)
(33, '13007039', '13007039', '林彥龍', None, None, None, None, '', '管理者', '', '', None)
(34, '13007040', '13007040', '高殿凱', None, None, None, None, None, '學生', None, None, None)
(35, '13007041', '13007041', '莊騏嘉', None, None, None, None, None, '學生', None, None, None)
(36, '13007046', '13007046', '鄧宇庭', None, None, None, None, None, '學生', None, None, None)
(37, '13007001', '13007001', '王怡蓁', None, None, '', None, '13', '學生', None, None, None)
MySQL connection is closed

[Done] exited with code=0 in 0.859 seconds
```

---
ESP32 程式
===
---
## Blinking an LED With ESP32


```
const int ledPin = 2; //IO2

void setup() {
  // put your setup code here, to run once:
  pinMode (ledPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite (ledPin, HIGH);

  delay(500);

  digitalWrite (ledPin, LOW);

  delay(500);
}

```

## WIFI 連線 

Wifi模式
用WiFi.h程式庫會有4種wifi模式可以用:
| 語法  | WIFI模式 | 功能 | 
| --- | ----- | ----- |	
|WiFi.mode(WIFI_AP);|	Access Point (AP)|	ESP32可以讓其他設備透過wifi接入(就像家裡的wifi基地台，可供手機連線)。|
|WiFi.mode(WIFI_STA);|	Station(STA)|	無線終端模式，也就是讓ESP32可以連接上其他的熱點(就像手機一樣，可以連上家裡wifi)。|
|WiFi.mode(WIFI_AP_STA);|	AP+STA|	將ESP32設置成兩個模式並存。|
|WiFi.mode(WIFI_OFF);|	OFF|	關閉wifi|

1. 通常我們都會將ESP32設置成STA模式，連接家裡wifi基地台，這樣手機連接wifi基地台，也可以連上ESP32。
2. 連接到時間伺服器的 NTPClient 從 NTP 伺服器取得時間並保持同步。

``` arduino
#include <NTPClient.h>
// change next line to use with another board/shield
// #include <ESP8266WiFi.h>
#include <WiFi.h> // for WiFi shield
//#include <WiFi101.h> // for WiFi 101 shield or MKR1000
#include <WiFiUdp.h>

const char ssid[] = "Aki";      //WiFi網路名稱
const char pwd[] = "12345678";  //WiFi密碼
const int ledPin = 2;
int wifi_test = 0;
int wifi_print_cnt = 0;

WiFiUDP ntpUDP;
// By default 'pool.ntp.org' is used with 60 seconds update interval and
// no offset
NTPClient timeClient(ntpUDP);

//char ssid[] = "RPi-vbird";       // network SSID (name)
//char pass[] = "xxxxxxxxx";       // network password 
IPAddress dns1(120,114,100,  1); // first DNS server
IPAddress dns2(  8,  8,  8,  8); // second DNS server
char ntpserver[] = "ntp.ksu.edu.tw";  // NTP 伺服器
int GMT = +8;
//Week Days
String weekDays[7]={"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

//Month names
String months[12]={"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

// You can specify the time server pool and the offset, (in seconds)
// additionally you can specify the update interval (in milliseconds).
// NTPClient timeClient(ntpUDP, "europe.pool.ntp.org", 3600, 60000);

int status = WL_IDLE_STATUS;  // the WiFi radio's status

void setup() {
  // put your setup code here, to run once:
  pinMode (ledPin, OUTPUT);
  Serial.begin(115200);

  WiFi.mode(WIFI_STA);  //設置WiFi模式
  WiFi.begin(ssid, pwd);

  Serial.println("WiFi connecting");

  //當WiFi連線時會回傳WL_CONNECTED，因此跳出迴圈時代表已成功連線
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println("WiFi connected");

  // 連上 AP 之後才開始設定好 DNS
// Initialize a NTPClient to get time

  timeClient.begin();
  // Set offset time in seconds to adjust for your timezone, for example:
  // GMT +1 = 3600
  // GMT +8 = 28800
  // GMT -1 = -3600
  // GMT 0 = 0
  timeClient.setTimeOffset(28800); //台灣時區要用28800
}

void loop() {
  wifi_print_cnt = wifi_print_cnt + 1;
  if (wifi_print_cnt  >= 10 ){
    wifi_print_cnt = 0;
    printwifidata(); 
    timeClient.update();
    Serial.println(timeClient.getFormattedTime()); 
    printtime();
  }
  // put your main code here, to run repeatedly:
    digitalWrite (ledPin, HIGH);
    delay(500);
    digitalWrite (ledPin, LOW);
    delay(500);
}

void printtime(){
  timeClient.update();

  time_t epochTime = timeClient.getEpochTime();
  Serial.print("Epoch Time: ");
  
    Serial.println(epochTime);          //Epoch Time:1728400116
  String formattedTime = timeClient.getFormattedTime();


  Serial.print("Formatted Time: ");
  Serial.println(formattedTime);      //Formatted Time: 15:08:36

  int currentHour = timeClient.getHours();
  Serial.print("Hour: ");
  Serial.println(currentHour);        //Hour: 15

  int currentMinute = timeClient.getMinutes();
  Serial.print("Minutes: ");
  Serial.println(currentMinute);      //Minutes: 8
   
  int currentSecond = timeClient.getSeconds();
  Serial.print("Seconds: ");
  Serial.println(currentSecond);      //Seconds: 36

  String weekDay = weekDays[timeClient.getDay()];
  Serial.print("Week Day: ");
  Serial.println(weekDay);            //Week Day: Tuesday

  //Get a time structure
  struct tm *ptm = gmtime ((time_t *)&epochTime); 

  int monthDay = ptm->tm_mday;
  Serial.print("Month day: ");
  Serial.println(monthDay);           //Month day: 8

  int currentMonth = ptm->tm_mon+1;
  Serial.print("Month: ");
  Serial.println(currentMonth);       //Month: 10

  String currentMonthName = months[currentMonth-1];
  Serial.print("Month name: ");
  Serial.println(currentMonthName);   //Month name: October

  int currentYear = ptm->tm_year+1900;
  Serial.print("Year: ");
  Serial.println(currentYear);        //Year: 2024

  //Print complete date:
  String currentDate = String(currentYear) + "-" + String(currentMonth) + "-" + String(monthDay);
  Serial.print("Current date: ");
  Serial.println(currentDate);        //Current date: 2024-10-8
  Serial.println("");
}

void printwifidata() {
  Serial.println("--------------------------");
  Serial.print("IP位址:");
  Serial.println(WiFi.localIP());  //讀取IP位址

  Serial.print("GW address: ");
  Serial.println(WiFi.gatewayIP());
  
  Serial.print("DNS address: ");
  Serial.println(WiFi.dnsIP());

  Serial.print("WiFi RSSI: ");
  Serial.print(WiFi.RSSI());  //讀取WiFi強度
  Serial.println("dBm");  

  Serial.print("ESP32 MAC Address: ");
  Serial.println(WiFi.macAddress());
}

```



### 打開序列埠監控視窗就可以看到ESP32所分配到的IP位址以及WiFi強度。

```
rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
configsip: 0, SPIWP:0xee
clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
mode:DIO, clock div:1
load:0x3fff0030,len:4604
ho 0 tail 12 room 4
load:0x40078000,len:15488
load:0x40080400,len:4
load:0x40080404,len:3180
entry 0x400805b8
WiFi connecting
.WiFi connected

IP位址:172.20.10.8
GW address: 172.20.10.1
DNS address: 172.20.10.1
WiFi RSSI: -31dBm
ESP32 MAC Address: FC:E8:C0:7A:DE:70
15:19:21
Epoch Time: 1728400761
Formatted Time: 15:19:21
Hour: 15
Minutes: 19
Seconds: 21
Week Day: Tuesday
Month day: 8
Month: 10
Month name: October
Year: 2024
Current date: 2024-10-8
```






網頁設計
===
建立智慧家庭操作網頁，並使用 **Arduino** 為每個 **NodeMCU-32S** 設計控制程式。以下是具體步驟：

### 1. **資料庫設計（MySQL）**

設計一個 MySQL 資料庫來儲存來自各 NodeMCU-32S 的感測器數據與控制狀態。根據需求，資料庫中應包含一個 `device` 資料表來管理設備狀態。

```sql
CREATE DATABASE smart_home;

USE smart_home;

CREATE TABLE device (
    id INT AUTO_INCREMENT PRIMARY KEY,
    device_name VARCHAR(50),
    location VARCHAR(50),
    sensor_type VARCHAR(50),
    sensor_value FLOAT,
    control_status BOOLEAN,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2. **Django 設定**

#### a. **建立 Django 專案與應用**

首先，啟動 Django 專案並配置資料庫連接。

```bash
django-admin startproject smart_home_project
cd smart_home_project
python manage.py startapp control_panel
```

在 `settings.py` 中配置 MySQL 資料庫連接：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'smart_home',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### b. **建立 Django 模型**

在 `models.py` 中，設置對應的設備模型：

```python
from django.db import models

class Device(models.Model):
    device_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    sensor_type = models.CharField(max_length=50)
    sensor_value = models.FloatField()
    control_status = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.device_name} ({self.location})"
```

然後執行遷移命令：

```bash
python manage.py makemigrations
python manage.py migrate
```

#### c. **建立操作網頁與 API**

在 `views.py` 中，設計一個簡單的 API 來處理設備狀態的更新和顯示。

```python
from django.shortcuts import render
from django.http import JsonResponse
from .models import Device

def device_status(request):
    devices = Device.objects.all()
    return render(request, 'device_status.html', {'devices': devices})

def update_device(request, device_id):
    device = Device.objects.get(id=device_id)
    new_status = request.POST.get('control_status')
    device.control_status = bool(new_status)
    device.save()
    return JsonResponse({'status': 'success'})
```

在 `urls.py` 中配置路由：

```python
from django.urls import path
from . import views

urlpatterns = [
    path('status/', views.device_status, name='device_status'),
    path('update/<int:device_id>/', views.update_device, name='update_device'),
]
```

#### d. **前端操作界面**

使用 HTML 與 JavaScript 來建立即時控制介面，顯示各設備的狀態並讓使用者可以進行控制。

```html
<!-- device_status.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Smart Home Control Panel</title>
</head>
<body>
    <h1>Smart Home Control Panel</h1>
    <div>
        {% for device in devices %}
            <p>{{ device.device_name }} ({{ device.location }}) - Sensor: {{ device.sensor_value }} 
            <button onclick="toggleDevice({{ device.id }}, {{ device.control_status }})">
                {{ device.control_status|yesno:"ON,OFF" }}
            </button></p>
        {% endfor %}
    </div>

    <script>
        function toggleDevice(device_id, current_status) {
            const new_status = current_status ? 0 : 1;
            fetch(`/update/${device_id}/`, {
                method: 'POST',
                body: JSON.stringify({ control_status: new_status }),
                headers: { 'Content-Type': 'application/json' },
            }).then(response => response.json()).then(data => {
                if (data.status === 'success') {
                    location.reload();
                }
            });
        }
    </script>
</body>
</html>
```

### 3. **Arduino 控制程式（NodeMCU-32S）**

每個 NodeMCU-32S 模組會根據不同的功能需求撰寫控制程式。以頂樓水塔液位偵測為例：

```cpp
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "your_wifi_ssid";
const char* password = "your_wifi_password";
const char* serverName = "http://192.168.68.115/update/";

int sensorPin = A0; // 液位感測器的引腳
int sensorValue = 0;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  sensorValue = analogRead(sensorPin);
  if (sensorValue < 500) {
    sendData(1);  // 水位過低，發送狀態
  } else {
    sendData(0);  // 水位正常
  }
  delay(10000);  // 每10秒檢測一次
}

void sendData(int status) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    String url = String(serverName) + "1";  // 假設設備ID是1
    http.begin(url);
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    
    String postData = "control_status=" + String(status);
    int httpResponseCode = http.POST(postData);
    
    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println(httpResponseCode);
      Serial.println(response);
    }
    http.end();
  }
}
```

此程式每 10 秒讀取液位感測器數據，並根據狀態上傳至伺服器。

### 4. **功能擴展**

根據不同功能，例如 PM2.5 偵測、溫度偵測與冷氣控制，依此模組撰寫對應的 Arduino 程式來控制繼電器或紅外線發射器，並在 Django 網頁介面中實現控制與即時監控功能。


登入頁面設計
===
使用 **Python**, **Django**, **MySQL** 和 **Synology NAS** 架設登入系統的步驟，並在不同裝置上使用響應式動態網頁設計技術進行操作。

### 1. **系統架構概述**
- **伺服器**: Synology DS920+ NAS
- **IP 設定**:
  - NAS IP: `192.168.68.115`
  - NodeMCU-32S IP 範圍: `192.168.68.116 - 192.168.68.123`
  - 對外網路網址: `aki920p.myds.me`
- **系統使用技術**:
  - **後端**: Python, Django, MySQL
  - **前端**: HTML, CSS, JavaScript，採用響應式設計

### 2. **資料庫設計**

首先在 MySQL 中創建一個名為 `db_25` 的資料庫，並創建 `user` 資料表來儲存使用者帳號和密碼。

```sql
CREATE DATABASE db_25;

USE db_25;

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

### 3. **Django 專案設定**

#### a. **建立 Django 專案與應用**

```bash
django-admin startproject smart_home_system
cd smart_home_system
python manage.py startapp users
```

#### b. **設定資料庫連接**

在 `settings.py` 中，配置 MySQL 資料庫：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_25',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### c. **使用者模型**

在 `users/models.py` 中創建一個用來管理使用者登入的模型：

```python
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username
```

運行資料庫遷移：

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. **登入邏輯與視圖**

#### a. **表單與驗證**

在 `users/views.py` 中創建登入邏輯：

```python
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.utils import timezone
import time

failed_attempts = {}  # 記錄失敗次數的字典

def login_view(request):
    global failed_attempts
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        # 取得當前使用者IP地址
        user_ip = request.META.get('REMOTE_ADDR')
        
        # 判斷該IP是否已被鎖定
        if user_ip in failed_attempts and failed_attempts[user_ip]['count'] >= 3:
            time_left = 180 - (timezone.now() - failed_attempts[user_ip]['last_failed']).total_seconds()
            if time_left > 0:
                messages.error(request, f"輸入錯誤過多，請等待 {int(time_left)} 秒後再嘗試")
                return render(request, 'login.html')
            else:
                del failed_attempts[user_ip]  # 解除鎖定
        
        # 驗證使用者
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                return redirect('dashboard')  # 成功進入控制頁面
            else:
                raise User.DoesNotExist
        except User.DoesNotExist:
            messages.error(request, "帳號或密碼錯誤")
            
            # 更新失敗次數
            if user_ip not in failed_attempts:
                failed_attempts[user_ip] = {'count': 1, 'last_failed': timezone.now()}
            else:
                failed_attempts[user_ip]['count'] += 1
                failed_attempts[user_ip]['last_failed'] = timezone.now()
            
            if failed_attempts[user_ip]['count'] >= 3:
                messages.error(request, "輸入資料錯誤，已達三次限制，禁止登入 3 分鐘")
                
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'index2.html')
```

#### b. **URL 路由**

在 `users/urls.py` 中設定路由：

```python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
```

在 `smart_home_system/urls.py` 中包含這個應用的路由：

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]
```

#### c. **登入頁面 (login.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>智慧家庭系統登入</title>
    <style>
        /* 簡單的響應式樣式 */
        body { font-family: Arial, sans-serif; }
        .login-container { width: 100%; max-width: 400px; margin: 50px auto; padding: 20px; border: 1px solid #ccc; }
        input[type="text"], input[type="password"] { width: 100%; padding: 10px; margin: 5px 0; }
        input[type="submit"] { width: 100%; padding: 10px; background-color: #4CAF50; color: white; }
        .message { color: red; }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>歡迎使用智慧家庭系統</h2>
        {% if messages %}
            <div class="message">
                {% for message in messages %}
                    <p>{{ message }}</p>
                {% endfor %}
            </div>
        {% endif %}
        <form method="POST">
            {% csrf_token %}
            <label for="username">使用者帳號：</label>
            <input type="text" id="username" name="username" required>

            <label for="password">密碼：</label>
            <input type="password" id="password" name="password" required>

            <input type="submit" value="登入">
        </form>
    </div>
</body>
</html>
```

### 5. **部署在 Synology DS920+ 上**

1. 在 NAS 上安裝 **Web Station** 和 **MariaDB**，並配置 Python 環境來運行 Django 專案。
2. 使用 DSM 的 **Reverse Proxy** 功能，將內部服務暴露在 `aki920p.myds.me`。
3. 在 NAS 的網頁伺服器上配置 Django 專案，並確保所有依賴項已安裝。

### 6. **動態響應式設計**

登入頁面使用了基本的 CSS，並且設計為響應式，以便在不同設備上都能適應螢幕大小。


結案報告框架
===
### 1. Introduction (引言)

#### a. 背景說明
介紹智慧家庭系統的重要性，隨著物聯網 (IoT) 的發展，家居自動化已成為提升生活品質的關鍵。提到此專題的目的是運用 NodeMCU-32S 來實現不同環境下的自動化控制和監控，如水塔液位、空氣品質、溫度等。

#### b. 專題目標
目標是透過使用多個 NodeMCU-32S 裝置，整合感測器和控制器，並結合 Python 與 Django 建構的網站介面來遠端監控與操作。最終達成一個具備多種智慧家庭功能的整合系統。

### 2. Methods (方法)

#### a. 系統架構
概述系統的硬體架構，包括每個 NodeMCU-32S 的配置（根據你文件中提到的表格），例如水塔液位偵測、PM2.5 偵測與排風系統、溫度偵測與冷氣控制等。圖解會有助於說明系統架構。

#### b. 軟體設計
說明軟體部分的設計：
1. 使用 Arduino IDE 來編寫 NodeMCU-32S 的程式。
2. 使用 Python 和 Django 來建構網頁後端及使用者操作介面。資料會透過 Wi-Fi 傳送到 NAS 上的伺服器，並儲存到資料庫中。

#### c. 資料處理與通訊
解釋 ESP32S 如何通過 Wi-Fi 連接到伺服器、如何處理感測器的數據、並透過 Django API 來更新數據庫。特別是如何使用 LINEBOT 來通知使用者異常情況，如水塔液位過低或 PM2.5 指數過高。

### 3. Results (結果)

#### a. 系統功能實現
展示各 NodeMCU-32S 的具體功能，如水位偵測、PM2.5 偵測與排氣控制、溫度偵測與冷氣控制。這裡可以列舉測試過程中不同情境下系統的反應及性能表現。

#### b. 整合平台效果
展示 Django 網頁後台介面，說明用戶如何透過網頁檢視與控制各設備的運作狀況，並描述使用者透過 LINEBOT 接收即時通知的效果。

#### c. 效能與可靠性
總結測試中系統的穩定性、反應速度及可靠性，並列出一些具體測試數據或報告圖表，例如溫度控制的準確性或液位偵測的反應時間。

### 4. Discussion (討論)

#### a. 成果分析
討論系統成功實現的功能，以及遇到的挑戰（如 Wi-Fi 連線不穩或感測器精度問題）。可以指出系統在現實場景中的可行性及未來應用前景。

#### b. 系統優化與未來發展
提出系統優化的方向，例如提升感測器靈敏度、增加其他智慧家庭應用的整合（如光線控制或智慧門鎖）。同時，也可以探討如何擴展此系統，應用於更大規模的智能建築或商業空間。

#### c. 結論
總結專題的成果，重申此智慧家庭系統具備的實用性和創新點，並表達未來持續改進與應用的期許。

---
