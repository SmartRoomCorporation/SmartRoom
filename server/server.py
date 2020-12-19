import paho.mqtt.client as mqtt
from pprint import pprint
from SmartRoomClient import SmartRoomClient

smartrooms = [] # list of clients connected

def on_connect(client, userdata, flags, rc): # on connect callback
    print("Server Started")
    client.subscribe("subreqq")

def on_message(client, userdata, msg): # on message callback
    if(str(msg.topic) == "subreqq"):
        add_mqtt_client(str(msg.payload.decode("utf-8")))

def add_mqtt_client(topic):
    clientTopic = topic
    print("Client requested connection with topic: " + clientTopic)
    sr = SmartRoomClient()
    sr.setMacAddress(clientTopic)
    smartrooms.append(sr)
    client.publish(clientTopic, "Subscribed on " + clientTopic, qos=0, retain=False)
    client.subscribe(clientTopic)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("87.16.33.82", 1883, 60)


client.loop_forever() # loop