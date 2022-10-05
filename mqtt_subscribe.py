import paho.mqtt.client as mqtt
import time

def mqtt_subscribe(user, passwd, server, port, topic):

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code => "+mqtt.connack_string(rc))

    def on_subscribe(client, userdata, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))
    
    def on_message(client, userdata, msg):
        print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic)
    
    
    client = mqtt.Client()
    client.on_subscribe = on_subscribe
    client.on_message = on_message

    client.on_connect = on_connect

    try:
        client.username_pw_set(username=user, password=passwd)
        client.connect(server, port)
    except:
        print("Connection Failed")

    try:
        client.subscribe(topic, qos=0)
        client.loop_start()


    except KeyboardInterrupt:
        client.loop_stop()
        client.unsubscribe(topic)
        client.disconnect()
        print("Done.")