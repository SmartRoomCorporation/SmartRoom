import paho.mqtt.client as mqtt
from uuid import getnode as get_mac
import json
from threading import Thread
import logging

log = logging.getLogger("MQTT_LOG_DEBUG")
topic = ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))
serverTopic = ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))+'-server' # output from client
GETSTATUS = "GETSTATUS"

class SmartRoom(Thread):
    sensors = dict()
    client = mqtt.Client()
    ip = None
    port = 1883
    camera = None
    ttl = 60
    configFile = "smartroom.conf"

    def setPort(self, port):
        self.port = port

    def setTtl(self, ttl):
        self.ttl = ttl

    def setIp(self, ip):
        self.ip = ip

    def setCamera(self, camera):
        self.camera = camera

    def getCamera(self):
        return self.camera

    def addSensor(self, sensor, sensorobj):
        self.sensors[sensor] = sensorobj

    def getSensor(self, sensor):
        if(sensor in self.sensors): return self.sensors.get(sensor)
        return False

    def getSensorsList(self):
        return self.sensors
    
    def initClient(self):
        if(self.ip is not None):
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.on_publish = self.on_publish
            self.client.enable_logger(logger=log)
            self.client.on_log = self.on_log
            self.client.connect(self.ip, self.port, self.ttl)
            self.client.loop_start()

    def getRoomStatus(self):
        currStatus = dict()
        for key, value in self.sensors.items():
            currVal = value.startMeasure()
            value.actuator()
            currAct = value.getActuatorStatus()
            autopilot = value.getAutopilot()
            currStatus[key] = (currVal, currAct, autopilot)
        return currStatus

    def on_connect(self, client, userdata, flags, rc): # on connect callback
        client.subscribe(str(topic))
        client.publish("subreqq", topic, qos=0, retain=False)

    def on_message(self, client, userdata, msg): # on message callback
        if(msg.topic == topic):
            if(str(msg.payload.decode("utf-8")) == GETSTATUS):
                client.publish(serverTopic, json.dumps(self.getRoomStatus()), qos=0, retain=False)
            if(str(msg.payload.decode("utf-8")) == "ciaone"):
                print("ciaone")

    def on_publish(self, client, userdata, mid): # on publish callback
        return True

    def on_log(self, client, userdata, level, buf):
        print(buf)

    def pubToServ(self):
        return self.getRoomStatus()

    def run(self):
        self.initClient()

    def stopClient(self):
        self.client.loop_stop()
        self.client.disconnect()