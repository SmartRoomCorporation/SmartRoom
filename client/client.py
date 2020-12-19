import paho.mqtt.client as mqtt
from uuid import getnode as get_mac
topic = ':'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))

def on_connect(client, userdata, flags, rc): # on connect callback
    print("Connected with result code "+str(rc))
    client.subscribe(str(topic))
    client.publish("subreqq", topic, qos=0, retain=False)

def on_message(client, userdata, msg): # on message callback
    if(msg.topic == topic):
        print(str(msg.payload.decode("utf-8")))  

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("87.16.33.82", 1883, 60)


client.loop_forever() # client loop, handles reconnect