import paho.mqtt.client as mqtt
import time


def mqtt_publish(user, passwd, server, port, topic, msg, iter):

    def on_publish(client, userdata, mid):
        print("Message publish " + str(mid) )

    client = mqtt.Client()
    client.on_publish = on_publish


    try:
        client.username_pw_set(username=user, password=passwd)
        client.connect(server, port)
    except:
        print("Connection Failed")



    for i in range (0, iter, 1):
        (rc, mid) = client.publish(topic=topic, payload=msg, qos=0)
        print("Error return from publish: " + mqtt.error_string(rc))
        time.sleep(2)