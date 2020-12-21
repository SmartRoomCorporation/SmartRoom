import paho.mqtt.client as mqtt
from pprint import pprint
from SmartRoomClient import SmartRoomClient
import json

# clientTopic input from client
# serverTopic output from server

smartrooms = dict() # list of clients connected

def on_connect(client, userdata, flags, rc): # on connect callback
    print("Server Started")
    client.subscribe("subreqq")

def on_message(client, userdata, msg): # on message callback
    if(str(msg.topic) == "subreqq"):
        add_mqtt_client(str(msg.payload.decode("utf-8")))
    if(sanitizeTopic(str(msg.topic)) in smartrooms): 
        if(str(msg.payload.decode("utf-8")) == "ciao"): 
            client.publish(sanitizeTopic(str(msg.topic)), "ciaone", qos=0, retain=False)
            return True
        smartrooms[sanitizeTopic(str(msg.topic))].updateSensors(json.loads(str(msg.payload.decode("utf-8"))))
        #print(json.loads(str(msg.payload.decode("utf-8"))))
        printSensors(sanitizeTopic(str(msg.topic)))

def add_mqtt_client(topic):
    clientTopic = topic
    serverTopic = topic+'-server'
    print("Client requested connection with topic: " + clientTopic)
    sr = SmartRoomClient()
    sr.setMacAddress(clientTopic)
    smartrooms[clientTopic] = sr
    client.publish(clientTopic, "Subscribed on " + clientTopic, qos=0, retain=False)
    client.subscribe(serverTopic)
    print(serverTopic)
    client.publish(clientTopic, "GETSTATUS", qos=0, retain=False)

def sanitizeTopic(topic):
    return topic[0:len(topic)-7] 

def printSensors(smartroom):
    smsensors = smartrooms[smartroom].getSensorsList()
    for key, value in smsensors.items():
        print(str(key) + " " + str(value))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("87.7.152.200", 1883, 60)


client.loop_forever() # loop