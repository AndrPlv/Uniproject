#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <iarduino_DHT.h>

#define DHTPIN 2

LiquidCrystal_I2C lcd(0x27, 16, 2);
iarduino_DHT sensor(DHTPIN);
void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
}

void lcd_print(int t,int h){
  lcd.clear();
  
  lcd.setCursor(4, 0);
  lcd.print("Tem:");
  lcd.setCursor(4, 1);
  lcd.print("Hum:");

  lcd.setCursor(10, 0);
  lcd.print(t);
  lcd.setCursor(10, 1);
  lcd.print(h);  
  
  
  
}
void loop() {
  digitalWrite(13, HIGH);
  delay(500);
  // put your main code here, to run repeatedly:
  if (sensor.read() == DHT_OK) {
      Serial.print(sensor.hum);
      Serial.print(',');
      Serial.println(sensor.tem);
      lcd_print(sensor.tem, sensor.hum);
   }
   
  
  digitalWrite(13, LOW);
  delay(500);
}