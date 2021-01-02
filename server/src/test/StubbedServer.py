import paho.mqtt.client as mqtt
from threading import Thread
from uuid import getnode as get_mac
import json

class StubbedServer():

    clientTopic = None
    serverTopic = None

    def on_connect(self, client, userdata, flags, rc): # on connect callback
        client.subscribe("subreqq")

    def setTopic(self, topic):
        self.clientTopic = topic
        self.serverTopic = topic + '-server'
        self.server.subscribe(self.serverTopic)

    def getClientTopic(self):
        return self.clientTopic

    def on_message(self, client, userdata, msg): # on message callback
        print(str(msg.payload.decode("utf-8")))
        clientTopic = getClientTopic()
        print(clientTopic)
        if(msg.topic == "subreqq"): setTopic(str(msg.payload.decode("utf-8")))
        if(str(msg.payload.decode("utf-8")) == "TESTAUTOPILOT"):
            data = ["Temperature", "AUTOOFF"]
            message = ["COMMAND", data]
            client.publish(clientTopic, json.dumps(message), qos=0, retain=False)
        elif(str(msg.payload.decode("utf-8")) == "TESTRISE"):
            data = ["Air", "RISE"]
            message = ["COMMAND", data]
            client.publish(clientTopic, json.dumps(message), qos=0, retain=False)
        elif(str(msg.payload.decode("utf-8")) == "TESTREDUCE"):
            data = ["Light", "REDUCE"]
            message = ["COMMAND", data]
            client.publish(clientTopic, json.dumps(message), qos=0, retain=False)
        elif(str(msg.payload.decode("utf-8")) == "TESTCOMMAND"):
            data = ["Air", "ACTUATOR", "FANUP"]
            message = ["COMMAND", data]
            client.publish(clientTopic, json.dumps(message), qos=0, retain=False)
        elif(str(msg.payload.decode("utf-8")) == "STOP"):
            client.loop_stop()
            client.disconnect()

    def __init__(self):
        self.server = mqtt.Client()
        self.server.on_message = self.on_message
        self.server.on_connect = self.on_connect
        self.server.connect("87.7.152.200", 1883, 60)
        self.server.loop_forever()

s = StubbedServer()