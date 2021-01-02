import paho.mqtt.client as mqtt
from pprint import pprint
import os,sys,inspect
script_dir = os.path.dirname(__file__)
sys.path.insert(0, script_dir)
from SmartRoomClient import SmartRoomClient
import json
import logging
from threading import Thread
import time

log = logging.getLogger("MQTT_LOG_DEBUG")
GETSTATUS = "GETSTATUS"
SENSORSLIST = "SENSORSLIST"
UPDATESENSOR = "UPDATESENSOR"
SUBSCRIBED = "SUBSCRIBED"

# clientTopic input from client
# serverTopic output from server

#configFile = "smartroom.conf"


class SmartroomServer(Thread):
    smartrooms = dict() # list of clients connected
    ip = "127.0.0.1"
    port = 1883
    ttl = 60
    server = mqtt.Client()

    def setPort(self, port):
        self.port = port

    def setTtl(self, ttl):
        self.ttl = ttl

    def setIp(self, ip):
        self.ip = ip

    def getPort(self):
        return self.port

    def getTtl(self):
        return self.ttl

    def getIp(self):
        return self.ip

    def initServer(self):
        if(self.ip is not None):
            self.server.on_connect = self.on_connect
            self.server.on_message = self.on_message
            self.server.on_publish = self.on_publish
            self.server.enable_logger(logger=log)
            self.server.on_log = self.on_log
            self.server.connect(self.ip, self.port, self.ttl)
            self.server.loop_start()

    def run(self):
        self.initServer()

    def stopServer(self):
        self.server.loop_stop()
        self.server.disconnect()

    def getSmartRoomClient(self, topic):
        if(topic in self.smartrooms): return self.smartrooms[topic]
        else: return None

    def getServer(self):
        return self.server

    def getSmartRooms(self):
        return self.smartrooms

    def addSmartRoomClient(self, clientTopic, sr):
        self.smartrooms[clientTopic] = sr

    def on_connect(self, client, userdata, flags, rc): # on connect callback
        print("Server Started") # on file
        client.subscribe("subreqq")

    def on_log(self, client, userdata, level, buf):
            print(buf)

    def on_message(self, client, userdata, msg): # on message callback
        if(str(msg.topic) == "subreqq"):
            self.add_mqtt_client(str(msg.payload.decode("utf-8")))
        else: self.decodeMessage(str(msg.topic), json.loads(str(msg.payload.decode("utf-8"))))

    def on_publish(self, client, userdata, mid): # on publish callback
        return True

    def add_mqtt_client(self, topic):
        clientTopic = topic
        serverTopic = topic+'-server'
        print("Client requested connection with topic: " + clientTopic) # on file
        sr = SmartRoomClient(self)
        sr.setMacAddress(clientTopic)
        self.addSmartRoomClient(clientTopic, sr)
        sub = [SUBSCRIBED, clientTopic]
        self.server.publish(clientTopic, json.dumps(sub), qos=0, retain=False)
        self.server.subscribe(serverTopic)
        self.server.publish(clientTopic, json.dumps(GETSTATUS), qos=0, retain=False)

    def sanitizeTopic(self, topic):
        return topic[0:len(topic)-7]

    def decodeMessage(self, topic, request):
        sr = self.getSmartRoomClient(self.sanitizeTopic(topic))
        if(sr is None): return False # TODO raise Exception
        data = request.pop()
        request = request[0]
        if(request == SENSORSLIST):
            for key, value in data.items():
                sr.addSensor(key, value)
            return False
        if(request == UPDATESENSOR):
            for key, value in data.items():
                sr.updateSensor(key, value)
            return False

    def sendCommand(self, topic, command):
        self.server.publish(topic, json.dumps(command), qos = 0, retain = False)

    def printSrSensors(self, sr):
        for key, value in sr.getSensorsList().items():
            pprint(key)
            pprint(value.getCurrentValue())
            pprint(value.getThresholdValue())
            pprint(value.getActuator())
            pprint(value.getAutopilot())
