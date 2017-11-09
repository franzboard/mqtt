#!/usr/bin/env python3
"""
    Publish ds1820 temperatura data
    to mqtt broker
"""
import os 
import time
import paho.mqtt.client as mqtt
import sys, signal
from ds1820 import getTemp

TOPIC ="ds1820-temperature"
HOST = "test.mosquitto.org"
USER= ""
PASS =""
PORT = 1883

def signal_handler(signal, frame):
    print("\nprogram exited")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def on_connect(client, userdata, flags, rc):
    pass
   # print("rc: " + str(rc))

def on_publish(client, obj, mid):
    pass
   # print("mid: " + str(mid))

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

#client.on_log = on_log

# not needed for test.mosquitto
# client.username_pw_set(USER, PASS)
client.connect(HOST, PORT)

if __name__ == "__main__":
    while True:
        result = getTemp()
        for dev, temp in result.items():
            msg = "{} -> {:6.2f} °C".format(dev, temp)
            client.publish(TOPIC, msg)
        time.sleep(5)

