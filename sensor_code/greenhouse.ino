#include<DHT.h>
#include<SoftwareSerial.h>
#include<ArduinoJson.h>
#include<Servo.h>

#define DHTPIN 2
#define DHTTYPE DHT11
const int waterpump = 10;

SoftwareSerial espSerial(5, 6);
DHT dht(DHTPIN, DHTTYPE);
Servo servo;

int temp;
int humd;
int moist;
bool air_vent = false;
bool water_pump = false;
String str;

void setup(){
  Serial.begin(9600);
  espSerial.begin(9600);
  dht.begin();
  pinMode(waterpump, OUTPUT);  
  servo.attach(9, 500, 2500);
}


void loop(){
  //----------------------------------------------------------
  // Get the data from the sensors
  temp = dht.readTemperature();
  humd = dht.readHumidity();
  moist = 30.0;
  
  Serial.print("H: ");
  Serial.print(humd);
  Serial.print("% ");
  Serial.print(" T: ");
  Serial.print(temp);
  Serial.println("C");
  
  if(temp > 25 || humd < 60){
    //open the air vent since temperature or humidity is low
    Serial.println("Air Vent Open");
    if(!air_vent)
    servo.write(180);
    air_vent = true;
  }
  else{
    //close the air vent
    Serial.println("Air Vent Closed");
    if(air_vent)
    servo.write(1);
    air_vent = false;
  }

  if(moist < 40){
    //turn on the water pump
    Serial.println("Water Pump is On");
    if(!water_pump)
    digitalWrite(waterpump, HIGH);
    water_pump = true;
  }
  else{
    //turn off the water pump
    Serial.println("Water Pump is off");
    if(water_pump)
    digitalWrite(waterpump, LOW);
    water_pump = false;
  }
  //----------------------------------------------------------

  //----------------------------------------------------------
  // Send the data to Nodemcu through serial communication
  const size_t capacity = JSON_OBJECT_SIZE(5);
  DynamicJsonBuffer jsonBuffer(capacity);
  
  JsonObject& root = jsonBuffer.createObject();
  root["temperature"] = temp;
  root["moisture"] = moist;
  root["humidity"] = humd;
  root["air_vent"] = air_vent;
  root["water_pump"] = water_pump;
  root.printTo(Serial);
  root.printTo(espSerial);
  //----------------------------------------------------------
  
  delay(5000);
}
