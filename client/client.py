import paho.mqtt.client as mqtt
topic = ""

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("topicres")
    client.publish("topicreq", "topicreq", qos=0, retain=False)

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if(msg.topic == "topicres"):
        client.unsubscribe("topicres")
        topic = msg.payload
        client.subscribe(topic)
    if(msg.topic == topic):
        print(msg.payload)  
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("87.16.33.82", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()