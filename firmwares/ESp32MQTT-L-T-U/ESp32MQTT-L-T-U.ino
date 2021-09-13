#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include <ArduinoJson.h>
#include <SoftwareSerial.h>
const char* ssid = "TP-LINK_3FA28D";//SSID of the wifi
const char* password = "runkotobuki1121987";//password

byte MAC[6]; //mac address as array of byte
String mac = ""; //mac address as string
const char* mqtt_server = "79.12.248.28";//IP of MQTT server

char* subTopicLight = "c4:4f:33:56:6d:c9-SUB"; //sub topic (used to receive commands)
char* pubTopicLight = "c4:4f:33:56:6d:c9-PUB"; //pub topic (used to send data)

String mac1 = "c5:3f:34:66:5d:c1";
char* subTopicTH = "c5:3f:34:66:5d:c1-SUB";
char* pubTopicTH = "c5:3f:34:66:5d:c1-PUB";

const char* sensorSub = "SENSORSUB";
boolean regLight = false;
boolean regTH = false;

const int SENDTIME = 5000;//5 s, time to wait to sand new data
int lightTime = 0; //starting time used for the time counter
int thTime = 0;

SoftwareSerial stSerial(19, 18); //RX, TX Serial communication with nucleo board
SoftwareSerial thpSerial(22, 23);
WiFiClient espClient; //client for wireless communication
PubSubClient client(espClient); //mqtt client

//message data
long lastMsg = 0;
char msg[10];

//nucleo64 status variables
int light = 0; //ammount of light measured
int setlight = 0; //value set for light

float temp = 0.0;
float hum = 0.0;
float pres = 0.0;
char *ptr;

//json message container
const size_t capacity = 1024;
DynamicJsonDocument receiveJson(capacity);

void setup() {
  Serial.begin(115200);//Serial communication for log information
  stSerial.begin(9600);
  thpSerial.begin(9600);//serial communication with nucleo 64 board
  setup_wifi();//function to setup the wireless communication
  client.setServer(mqtt_server, 1883);//set the parameters needed for mqtt communication
  client.setCallback(callback);//set the function used to select the operation when a message arrived
  lightTime = millis();//start counting time
  thTime = millis();
}

void loop() {
  //connection retry
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  readFromSerial();//read status from nucleo board
  readFromTHPSerial();
  //after 5s send data through mqtt communication
  sendLightData();
  sendTHData();
  delay (1000);
}

void sendLightData(){
  if(millis()-lightTime > SENDTIME){
    if(!regLight){
      if(millis()-lightTime > 20000){
        registrationLight();
        lightTime = millis();
      }
    }else{
      //creating json message  
      DynamicJsonDocument sendJson(capacity); 
      sendJson["msgType"] = "DATAMSG";
      sendJson["mac"] = "c4:4f:33:56:6d:c9";
      sendJson["type"] = "LIGHTMODULE";
      sendJson["data"]["light"] = light;
      sendJson["data"]["setlight"] = setlight;
      //convert json to serialized data(conversion to string)
      String output;
      serializeJson(sendJson, output);
      char out[output.length()+1];
      //send data through mqtt
      output.toCharArray(out, output.length()+1);
      client.publish(pubTopicLight, out);
      Serial.println("Dati inviati");
      ESP.getFreeHeap();
      lightTime = millis();//restart time counter
    }
  }
}

void sendTHData(){
  if(millis()-thTime > SENDTIME){
    if(!regTH){
      if(millis()-thTime > 20000){
        registrationTH();
        thTime = millis();
      }
    }else{
      //creating json message 
      DynamicJsonDocument sendJson(capacity);  
      sendJson["msgType"] = "DATAMSG";
      sendJson["mac"] = "c5:3f:34:66:5d:c1";
      sendJson["type"] = "TEMPHUMMODULE";
      sendJson["data"]["temperature"] = temp;
      sendJson["data"]["humidity"] = hum;
      //convert json to serialized data(conversion to string)
      String output;
      serializeJson(sendJson, output);
      char out[output.length()+1];
      //send data through mqtt
      output.toCharArray(out, output.length()+1);
      client.publish(pubTopicTH, out);
      Serial.println("Dati inviati");
      ESP.getFreeHeap();
      thTime = millis();//restart time counter
    }
  }
}

//read data from nucleo64 board
void readFromSerial(){
  if(stSerial.available()>0){
    stSerial.readBytes(msg, 10);
    light =((String)msg).toInt();
    Serial.println(light);
  }
}

void readFromTHPSerial(){
  if(thpSerial.available()>0){
    String str = thpSerial.readString();
    char strt[50];
    Serial.println("Ho ricevuto"+str);
    for(int i = 0; i < str.length(); i++){
      strt[i] = str[i];
    }
    ptr = strtok(strt, "#");
    if(ptr!=NULL){
      temp = atof(ptr);
      ptr = strtok(NULL, "#");
      if(ptr!=NULL)hum = atof(ptr);
      ptr = strtok(NULL, "#");
      if(ptr!=NULL)pres = atof(ptr);
    }
    Serial.println(temp);
    Serial.println(hum);
    Serial.println(pres);
  }
}
//setup wifi communication
void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  WiFi.macAddress(MAC);
  mac = byteArrayToHexString(MAC, 6);  
  Serial.println("MAC address: ");
  Serial.println(mac);
}

void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Message: ");
  String messageTemp;
  
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  
  Serial.println(); 
  //lettura del nuovo valore per la luce
  if (String(topic) == subTopicLight) {
    if(messageTemp.indexOf("CONFIRMSUB")>0){
      DynamicJsonDocument regJson(capacity);
      Serial.println("Send sensorreg");
      regJson["msgType"] = "SENSORREG";
      regJson["name"] = "LIGHTMODULE1";
      regJson["type"] = "LIGHTMODULE";
      regJson["mac"] = "c4:4f:33:56:6d:c9";
      String output;
      serializeJson(regJson, output);
      char out[output.length()+1];
      //send data through mqtt
      output.toCharArray(out, output.length()+1);
      client.publish(pubTopicLight, out);
      ESP.getFreeHeap();
    }else if(messageTemp.indexOf("CONFIRMREG")>0){
      regLight = true;
      Serial.println("Confirmation succeded");
    }else if(messageTemp.indexOf("COMMAND")>0){
      regLight = true;
      Serial.println("Confirmation succeded");
    }
    if(regLight){
      Serial.println("Ho ricevuto il comando");
      DeserializationError err = deserializeJson(receiveJson, messageTemp);
      if(err){
        Serial.println("Errore nella ricezione del comando json");
      }else{
        String msgType = receiveJson["msgType"];
        Serial.println(msgType);
          String s = receiveJson["command"]["setlight"];
          Serial.print(s);
          setlight = s.toInt();
          Serial.println(setlight);
          stSerial.print(setlight);
          Serial.println("Ho modificato il valore della luce");
      }
    }
  }else if(String(topic) == subTopicTH){
    if(messageTemp.indexOf("CONFIRMSUB")>0){
        DynamicJsonDocument regJson(capacity);
        Serial.println("Send sensorreg");
        regJson["msgType"] = "SENSORREG";
        regJson["name"] = "TEMHUMMODULE1";
        regJson["type"] = "TEMPHUMMODULE";
        regJson["mac"] = "c5:3f:34:66:5d:c1";
        String output;
        serializeJson(regJson, output);
        char out[output.length()+1];
        //send data through mqtt
        output.toCharArray(out, output.length()+1);
        client.publish(pubTopicTH, out);
        ESP.getFreeHeap();
    }else if(messageTemp.indexOf("CONFIRMREG")>0){
        regTH = true;
        Serial.println("Confirmation succeded");
    }else if(messageTemp.indexOf("COMMAND")>0){
        regTH = true;
        Serial.println("Confirmation succeded");
    }
    if(regTH){
        Serial.println("Ho ricevuto il comando");
        DeserializationError err = deserializeJson(receiveJson, messageTemp);
        if(err){
          Serial.println("Errore nella ricezione del comando json");
        }else{
          String msgType = receiveJson["msgType"];
          Serial.println(msgType);
          String s = receiveJson["command"]["setwh"];
          if(s.equals("true")){
            thpSerial.print(1);
            Serial.println("Ho acceso la caldaia");
          }else if(s.equals("false")){
            thpSerial.print(0);
            Serial.println("Ho spento la caldaia");
          }
        }
     }
  }
}
void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ESP32LightControl")) {
      Serial.println("connected");
      regLight = false;
      regTH = false;
      // Subscribe
      client.subscribe(subTopicLight);
      client.subscribe(subTopicTH);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      //Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

String byteArrayToHexString(byte* b, int len){
  String s = "";
  for(int i = 0; i < len; i++){
    if(b[i] < 0x10){
      s += '0';
    }
    s += String(b[i], HEX);
    if(i < len-1)s += ':';
  }
  return s;
}

void registrationLight(){
  char out[mac.length()];
  int i;
  for(i = 0; i <= mac.length(); i++){
    out[i]=mac[i];
  }
  Serial.println("Trying to register sensor");
  client.publish(sensorSub, out);
}

void registrationTH(){
  char out[mac1.length()];
  int i;
  for(i = 0; i <= mac1.length(); i++){
    out[i]=mac1[i];
  }
  Serial.println("Trying to register sensor");
  client.publish(sensorSub, out);
}
