# Instructions for Receiving and Sending Commands form PC to RPI3 using Wifi

## Install Mosquitto
    sudo apt-get install mosquitto
    sudo apt-get install mosquitto-clients
    
    
## Install Python Library for Mosquitto
    sudo -H pip install paho-mqtt
    sudo pip3 install paho-mqtt

The code consist of two clients, on each side and one broker, thus two different channel.


Channel 1 = Client-Broker-Client (For Sending Data form PC to RPI3)


Channel 2 = Client-Broker-Cleint (For Receveing Data form PC to RPI3)


## To Setup the Communication:

 1. Check the IP of the Broker/server through ifconfig and store it.
 2. Define the on_connect and on_message callbacks.
 3. Initialize the new instance of the Client class.
 4. Define the on_connect and on_message object of the client class with the callbacks defined above.
 5. Establish the connection to the Broker with broker's IP, port no.(usually 1883) and stayawake time(Default=60).
 6. Start the loop.
 7. Then start publishing the message through one of the client over one of the topics.

The message will be received by the second client over the second topic in the on_message callback, which can be processed thereafter.

For further [reference](http://www.steves-internet-guide.com/into-mqtt-python-client/)
