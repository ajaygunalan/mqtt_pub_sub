import paho.mqtt.client as mqtt
import logging
import random
#log_filename1="test1.log"
#log_filename2="test2.log"


MQTT_SERVER = "localhost"
MQTT_PATH_1 = "test_channel_1"
MQTT_PATH_2 = "test_channel_2"

# on_message is a callback function which is triggered when connection is made to the server/broker
def on_connect(client_1, userdata, flags, rc):
    print("Client_1 Connected with result code "+str(rc))
    client_1.subscribe(MQTT_PATH_1)

# on_message is a callback function which is triggered when message is recieved by the subscriber
def on_message(client_1, userdata, msg):
    print(msg.payload.decode("utf-8") )
    s.write(msg.payload.decode("utf-8")+"\n")

client_2 = mqtt.Client()    # Publishes through path2
client_1 = mqtt.Client()    #Subscribes through path1
client_1.on_connect = on_connect
client_1.on_message = on_message
client_1.connect(MQTT_SERVER, 1883, 60) #Connecting to the server/broker
client_2.connect(MQTT_SERVER, 1883, 60) #Connecting to the server/broker

client_1.loop_start()
 
j=1
while True:
    a=[j];
    for i in range(1,6):
       a.append(1*random.randint(1,i))
    client_2.publish(MQTT_PATH_2,str(a)) #Publishing an array of random digits
    j=j+1

