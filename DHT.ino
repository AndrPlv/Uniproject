#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <iarduino_DHT.h>

#define DHTPIN 2

int t,h;
bool link = false;

LiquidCrystal_I2C lcd(0x27, 16, 2);
iarduino_DHT sensor(DHTPIN);
void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(4, INPUT_PULLUP);
  pinMode(5, OUTPUT);
  Serial.begin(9600);
  digitalWrite(11, HIGH);
  lcd.init();
  lcd.backlight();
}

void lcd_print(int t,int h, bool link){
  lcd.clear();
  
  lcd.setCursor(0, 0);
  lcd.print("Tem:");
  lcd.setCursor(9, 0);
  lcd.print("Hum:");

  lcd.setCursor(5, 0);
  lcd.print(t);
  lcd.setCursor(14, 0);
  lcd.print(h);  

  lcd.setCursor(1,1);
  lcd.print("Link:");
  if (link) {
    lcd.setCursor(7,1);
    lcd.print("Wi-fi");
  }
  else {
    lcd.setCursor(7,1);
    lcd.print("COM-PORT");
  }
  
  
  
}
void loop() {
  digitalWrite(13, HIGH);
  delay(500);
  // put your main code here, to run repeatedly:
  if (not(digitalRead(4))) {
    link = !link;
  }
  
  if (sensor.read() == DHT_OK) {
      t = sensor.tem;
      h = sensor.hum;
      lcd_print(t, h, link);
   }

  if (not(link)) {
    Serial.print(t);
    Serial.print(",");
    Serial.println(h);
  }
  digitalWrite(13, LOW);
  delay(500);
}#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <iarduino_DHT.h>

#define DHTPIN 2

int t,h;
bool link = false;

LiquidCrystal_I2C lcd(0x27, 16, 2);
iarduino_DHT sensor(DHTPIN);
void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(4, INPUT_PULLUP);
  pinMode(5, OUTPUT);
  Serial.begin(9600);
  digitalWrite(11, HIGH);
  lcd.init();
  lcd.backlight();
}

void lcd_print(int t,int h, bool link){
  lcd.clear();
  
  lcd.setCursor(0, 0);
  lcd.print("Tem:");
  lcd.setCursor(9, 0);
  lcd.print("Hum:");

  lcd.setCursor(5, 0);
  lcd.print(t);
  lcd.setCursor(14, 0);
  lcd.print(h);  

  lcd.setCursor(1,1);
  lcd.print("Link:");
  if (link) {
    lcd.setCursor(7,1);
    lcd.print("Wi-fi");
  }
  else {
    lcd.setCursor(7,1);
    lcd.print("COM-PORT");
  }
  
  
  
}
void loop() {
  digitalWrite(13, HIGH);
  delay(500);
  // put your main code here, to run repeatedly:
  if (not(digitalRead(4))) {
    link = !link;
  }
  
  if (sensor.read() == DHT_OK) {
      t = sensor.tem;
      h = sensor.hum;
      lcd_print(t, h, link);
   }

  if (not(link)) {
    Serial.print(t);
    Serial.print(",");
    Serial.println(h);
  }
  digitalWrite(13, LOW);
  delay(500);
}
