import paho.mqtt.client as mqtt
from uuid import getnode as get_mac
import json
topic = ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))
GETSTATUS = "GETSTATUS"

class SmartRoom:
    sensors = dict()
    client = mqtt.Client()

    def addSensor(self, sensor, sensorobj):
        self.sensors[sensor] = sensorobj

    def getSensor(self, sensor):
        if(sensor in self.sensors): return self.sensors.get(sensor)
        return False

    def getSensorsList(self):
        return self.sensors
    
    def initClient(self, ip):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(ip, 1883, 60)
        self.client.loop_forever() 

    def getRoomStatus(self):
        currStatus = dict()
        for key, value in self.sensors.items():
            currStatus[key] = value.getCurrValue()
        return currStatus

    def on_connect(self, client, userdata, flags, rc): # on connect callback
        print("Connected with result code "+str(rc))
        client.subscribe(str(topic))
        client.publish("subreqq", topic, qos=0, retain=False)

    def on_message(self, client, userdata, msg): # on message callback
        if(msg.topic == topic):
            print(str(msg.payload.decode("utf-8")))  
            if(str(msg.payload.decode("utf-8")) == GETSTATUS):
                client.publish(json.dump(self.getRoomStatus()), topic, qos=0, retain=False)
