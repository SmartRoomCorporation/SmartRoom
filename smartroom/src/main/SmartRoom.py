import paho.mqtt.client as mqtt
from uuid import getnode as get_mac
import json
from threading import Thread
topic = ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))
serverTopic = ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))+'-server' # output from client
GETSTATUS = "GETSTATUS"

class SmartRoom(Thread):
    sensors = dict()
    client = mqtt.Client()
    ip = ""

    def addSensor(self, sensor, sensorobj):
        self.sensors[sensor] = sensorobj

    def getSensor(self, sensor):
        if(sensor in self.sensors): return self.sensors.get(sensor)
        return False

    def getSensorsList(self):
        return self.sensors
    
    def initClient(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.ip, 1883, 60)
        self.client.loop_start()

    def setIp(self, ip):
        self.ip = ip

    def getRoomStatus(self):
        currStatus = dict()
        for key, value in self.sensors.items():
            currStatus[key] = value.getCurrValue()
        return currStatus

    def on_connect(self, client, userdata, flags, rc): # on connect callback
        #print("Connected with result code "+str(rc))
        client.subscribe(str(topic))
        client.publish("subreqq", topic, qos=0, retain=False)

    def on_message(self, client, userdata, msg): # on message callback
        if(msg.topic == topic):
            #print(str(msg.payload.decode("utf-8")))  
            if(str(msg.payload.decode("utf-8")) == GETSTATUS):
                #print(json.dumps(self.getRoomStatus()))
                client.publish(serverTopic, json.dumps(self.getRoomStatus()), qos=0, retain=False)
            if(str(msg.payload.decode("utf-8")) == "ciaone"):
                print("ciaone")

    def pubToServ(self):
        self.client.publish(serverTopic, "ciao", qos=0, retain=False)

    def run(self):
        self.initClient()

    def stopClient(self):
        self.client.loop_stop()
        self.client.disconnect()