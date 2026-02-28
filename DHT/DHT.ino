#include <GyverNTP.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>
#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include <DHT.h>


#define DHTPIN 14        

LiquidCrystal_I2C lcd(0x27, 16, 2);
DHT dht(DHTPIN, DHT22);

const char* ssid = "Tenda_CBE978";     
const char* password = "Andrey0410";  
void setup() {
  pinMode(2, OUTPUT);     
  Serial.begin(115200);
  dht.begin();
  lcd.init();
  lcd.backlight(); 
  int test = 0;
  while(test<30) {
      WiFi.begin(ssid, password);  
      test ++;        
  }
  NTP.begin(7);
}

void loop() {
  NTP.updateNow();    
  digitalWrite(2, HIGH); 
  delay(500);
  
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  int result = send_value(t,h);
  lcd_print(t,h,result);
  
  digitalWrite(2, LOW);   
  delay(500);
}

void lcd_print(int t, int h, int result) {
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
  lcd.setCursor(6, 1);

  int status = WiFi.status();
  if ((status==3) and (result==200) ) {
    lcd.print("--->");
  }
  else if ((result == 400) or (result == 401) or (result == 402) or (result == 403) or (result == 404) or (result == 404)) {
    lcd.print("-XX>");
  }
  else if ((result == 500) or (result == 502) or (result == 503)) {
    lcd.print("<XX-");
  }
  else if (result == -1) {
    lcd.print("<??>");    
  }
  else {
    lcd.print("??->");
  }
} 
int send_value(float tem, float hum) {

  if ((WiFi.status() == 6) or (WiFi.status() == 4)) {
    int test = 0;
    while ((test <= 30) or not(WiFi.status() == 3)) {
      WiFi.begin(ssid, password);
      test ++;      
    }
  }      
  if (WiFi.status() == 3) {
    StaticJsonDocument<300> doc;
    
    doc["stID"] = WiFi.macAddress();     
    doc["Time"] = NTP.toString();
    doc["Temperature"] = tem;
    doc["Humidity"] = hum;
              
    WiFiClient client;
    HTTPClient http;  
    String jsonString;
    serializeJson(doc, jsonString);  
    http.begin(client, "http://192.168.0.104:5000/input");
    http.addHeader("Content-Type", "application/json");  

    int result = http.POST(jsonString);
    return result;
  }
  else {
    return 0;
  }
}