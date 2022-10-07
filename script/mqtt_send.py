import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time
import ssl
import certifi

def on_connect(client, userdata, flags, rc):
    print("Connected with result code => " + mqtt.connack_string(rc))

def on_message(client, userdata, msg):
    print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic + "' with QoS" + str(msg.qos))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_publish(client, userdata, mid):
    print("-- on_publish callback -- mid: " + str(mid))


client = mqtt.Client("GROUPE_DERMIGNY_PRONNIER_SENDER")
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_publish = on_publish
client.tls_set(r"P:\TP\ZZ2\Securite Systemes Embarques\Moustique\server.crt", tls_version=ssl.PROTOCOL_TLSv1_1)
client.tls_insecure_set(True)

try:
    #client.username_pw_set(username="UNDLOG",password="UNDPAS") #AZERGUES..20CHAMBRU26
    client.connect("172.16.32.7",8896)
    #client.will_set(topic='isima/GX/LEDs/LED1',payload="AUREVOIR")
    #client.subscribe("isima/GX")
except:
    print("Connection Failed")
    pass

client.loop_start()
while True:
    texte=input()
    (rc, mid) = client.publish(topic="/isima/GX/LEDs/LED1", payload=texte, qos=0)
