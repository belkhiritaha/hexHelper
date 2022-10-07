from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.asymmetric import x25519
import base64

import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe


def on_connect(client, userdata, flags, rc):
    print("Connected with result code => " + mqtt.connack_string(rc))

def on_message(client, userdata, msg):
    #print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic + "' with QoS" + str(msg.qos))

    #print(base64.b64decode(msg.payload))
    loaded_public_key = x25519.X25519PublicKey.from_public_bytes(base64.decodebytes(msg.payload))

    Bob_Shared_Key = Bob_private_key.exchange(loaded_public_key)

    print("\t - Shared Key compute by Bob : ", base64.encodebytes(Bob_Shared_Key).decode())
    pay = Bob_Public_Key_For_Alice.public_bytes(encoding=serialization.Encoding.Raw,format=serialization.PublicFormat.Raw)#.decode('utf-8').replace("-----BEGIN PUBLIC KEY-----\n","").replace("\n-----END PUBLIC KEY-----\n","").replace("MCowBQYDK2VuAyEA","")
    (rc, mid) = client.publish(topic="/ISIMA/S7_DH/GROUPE_Alice_Bob/PublicKeyServer", payload=base64.encodebytes(pay).decode(), qos=0)


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


Bob_private_key = X25519PrivateKey.generate()
Bob_public_key  = Bob_private_key.public_key()

B_public_key  = Bob_public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)
B_private_key = Bob_private_key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())


Bob_Public_Key_For_Alice = serialization.load_pem_public_key(bytes(B_public_key),backend=default_backend())




client = mqtt.Client("Bob")
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

try:
    client.connect("172.16.32.7", 1883)
except:
    print("Connection Failed")

client.subscribe("/ISIMA/S7_DH/GROUPE_Alice_Bob/PublicKeyIoT")

client.loop_forever()
