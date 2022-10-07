import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from challenge2 import *
import ssl
import certifi

def on_connect(client, userdata, flags, rc):
    print("Connected with result code => " + mqtt.connack_string(rc))

def on_message(client, userdata, msg):
    print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic + "' with QoS" + str(msg.qos))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

client = mqtt.Client("GROUPE_DERMIGNY_PRONNIER")
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.tls_set(r"P:\TP\ZZ2\Securite Systemes Embarques\Moustique\server.crt", tls_version=ssl.PROTOCOL_TLSv1_1)
client.tls_insecure_set(True)

#try:
#client.username_pw_set(username="OTHLOG",password="OTHPSW")
client.connect("172.16.32.7",8896)
client.subscribe("/ISIMA/TIBOPUTTY/#")
#publish("isima/GX", payload="SALU LAI JAN", qos=0, retain=False)
#except:
#    print("Connection Failed")

client.loop_forever()


"""
uGM2n0gNmCmEO/2IprxY2A==
+re6+fiIsaUJ3sOsXpKgxA==
"""

