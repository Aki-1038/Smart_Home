<?php
$esp32_ip = "192.168.68.96"; // 替換為ESP32的IP地址
$response = file_get_contents("http://$esp32_ip");
echo $response;
?>
