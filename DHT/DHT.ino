#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>
#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include <DHT.h>

// ТОЛЬКО ЭТУ СТРОЧКУ ПОМЕНЯЛ: D4 = GPIO2 (было 13, теперь 2)
#define DHTPIN 14        

LiquidCrystal_I2C lcd(0x27, 16, 2);
DHT dht(DHTPIN, DHT22);

const char* ssid = "Tenda_CBE978";     // Wi-Fi имя
const char* password = "Andrey0410";  // пароль

void setup() {
  // ПОМЕНЯЛ: D4 = GPIO2 для светодиода (было 13, теперь 2)
  pinMode(2, OUTPUT);     
  Serial.begin(115200);
  dht.begin();
  lcd.init();
  lcd.backlight();
  WiFi.begin(ssid, password);
}

void loop() {
  digitalWrite(2, HIGH);  // И тут поменял на 2
  delay(500);
  
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  lcd_print(t, h);
  delay(50);

  send_value(t,h);

  digitalWrite(2, LOW);   // И тут поменял на 2
  delay(500);
}

void lcd_print(int t, int h) {
  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print("Tem:");
  lcd.setCursor(9, 0);
  lcd.print("Hum:");
  lcd.setCursor(8, 0);
  lcd.print("|");  

  if (t >= 0) {
    lcd.setCursor(5, 0);
    lcd.print("+");   
    lcd.setCursor(6, 0);
    lcd.print(t);
  }
  else {
    lcd.setCursor(4, 0);
    lcd.print(t);
  }
  if (h != 100){
    lcd.setCursor(14, 0);
    lcd.print(h);
  }
  else {
    lcd.setCursor(13, 0);
    lcd.print(h);    
  }

  lcd.setCursor(0, 1);
  lcd.print("Client");
  lcd.setCursor(10, 1);
  lcd.print("Server");
  int status = WiFi.status();
  lcd.setCursor(6, 1);
  if (status == WL_CONNECTED) {
    lcd.print(">>>>");
  }
  else if (status == WL_CONNECT_FAILED) {    
    lcd.print(">!!>");
  }
  else if (status == WL_CONNECTION_LOST) {
    lcd.print("><>>");
  }
  else if (status == WL_DISCONNECTED) {
    lcd.print(">||>");
  }  
} 
void send_value(float tem, float hum) {
  
  StaticJsonDocument<200> doc;  // 200 байт — достаточно для наших данных
    
  doc["temperature"] = tem;
  doc["humidity"] = hum;
  doc["key"] = "password";
  WiFiClient client;
  HTTPClient http;  
  String jsonString;
  serializeJson(doc, jsonString);  
  http.begin(client, "http://192.168.0.104:5000/");
  http.addHeader("Content-Type", "application/json");  

  int result = http.POST(jsonString);
  Serial.print("Ответ: ");
  Serial.println(result);    
}