import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from challenge2 import *

def on_connect(client, userdata, flags, rc):
    print("Connected with result code => " + mqtt.connack_string(rc))

def on_message(client, userdata, msg):
    print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic + "' with QoS" + str(msg.qos))
    if not "GROUPE_XX" in msg.topic :
        client.publish(topic="/ISIMA/SECRET_SSIIAODF/CHALLENGE_2/DEFI_5/GROUPE_DERMIGNY_PRONNIER/LEDS/LED2", payload=msg.payload, qos=0)
        print("sault")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

client = mqtt.Client("GROUPE_DERMIGNY_PRONNIER")
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

try:
    client.username_pw_set(username="NOMOLO",password="NOMOPA")
    client.connect("172.16.32.7",10805)
    client.subscribe("/ISIMA/SECRET_SSIIAODF/CHALLENGE_2/DEFI_5/#")
    #publish("isima/GX", payload="SALUT LAI JAN", qos=0, retain=False)
except:
    print("Connection Failed")

client.loop_forever()


"""
uGM2n0gNmCmEO/2IprxY2A==
+re6+fiIsaUJ3sOsXpKgxA==
"""

