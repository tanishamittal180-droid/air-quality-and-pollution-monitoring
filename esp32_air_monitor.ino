#include <WiFi.h>
#include <DHT.h>

#define MQ135 34
#define MQ2 35

#define DHTPIN 4
#define DHTTYPE DHT22

#define LED 2
#define BUZZER 15

DHT dht(DHTPIN,DHTTYPE);

void setup()
{
Serial.begin(115200);

pinMode(LED,OUTPUT);
pinMode(BUZZER,OUTPUT);

dht.begin();
}

void loop()
{
int mq135=analogRead(MQ135);
int mq2=analogRead(MQ2);

float temp=dht.readTemperature();
float hum=dht.readHumidity();

int aqi=(mq135+mq2)/2;

String status;

if(aqi<=50)
status="Good";

else if(aqi<=100)
status="Moderate";

else if(aqi<=200)
status="Poor";

else
status="Hazardous";

if(aqi>200)
{
digitalWrite(LED,HIGH);
tone(BUZZER,1000);
}
else
{
digitalWrite(LED,LOW);
noTone(BUZZER);
}

Serial.println("----------------");
Serial.print("MQ135:");
Serial.println(mq135);

Serial.print("MQ2:");
Serial.println(mq2);

Serial.print("Temp:");
Serial.println(temp);

Serial.print("Humidity:");
Serial.println(hum);

Serial.print("AQI:");
Serial.println(aqi);

Serial.print("Status:");
Serial.println(status);

delay(3000);
}