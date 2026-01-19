#include <iarduino_DHT.h>

#define DHTPIN 2

iarduino_DHT sensor(DHTPIN);
void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (sensor.read() == DHT_OK) {
      Serial.print(sensor.hum);
      Serial.print(',');
      Serial.println(sensor.tem);
   }

  digitalWrite(13, HIGH);
  delay(500);
  
  digitalWrite(13, LOW);
  delay(500);
}