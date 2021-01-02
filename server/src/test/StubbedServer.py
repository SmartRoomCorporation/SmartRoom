import paho.mqtt.client as mqtt
from threading import Thread
from uuid import getnode as get_mac
import json

server = mqtt.Client()
clientTopic = ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))
serverTopic = ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))+'-server' # output from client

def on_connect(client, userdata, flags, rc): # on connect callback
    client.subscribe("subreqq")
    client.subscribe(serverTopic)

def on_message(client, userdata, msg): # on message callback
    print(str(msg.payload.decode("utf-8")))
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


server.on_message = on_message
server.on_connect = on_connect


server.connect("127.0.0.1", 1883, 60)
server.loop_forever()
