# mqtt_pub_sub
There is a server/broker and two clients on each side(Between Rpi and Ubuntu)
Step1: Install paho MQTT client for python using  "pip3 install paho-mqtt".
In this system we will be using One broker, two clients on each side and two different channels.
Steps to setup the communications:
 1. Check the IP of the Broker/server through ifconfig and store it.
 2. Define the on_connect and on_message callbacks.
 3. Initialize the new instance of the Client class.
 4. Define the on_connect and on_message object of the client class with the callbacks defined above.
 5. Establish the connection to the Broker with broker's IP, port no.(usually 1883) and stayawake time(Default=60).
 6. Start the loop.
 7. Then start publishing the message through one of the client over one of the topics.
The message will be recieved by the second client over the second topic in the on_message callback, which can be processed thereafter.

For further reference: http://www.steves-internet-guide.com/into-mqtt-python-client/

Author: Abhimanyu
Email ID: abhimanyusingh8713@gmail.com
