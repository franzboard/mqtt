#!/usr/bin/env python3
import os 
import time
import paho.mqtt.client as mqtt
import sys, signal

TOPIC ="pi-temperature"
HOST = "m23.cloudmqtt.com"
USER= "XXXX"
PASS ="XXXX"
PORT = 13462

def signal_handler(signal, frame):
    print("\nprogram exited")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def measure_temp():
    temp = os.popen('vcgencmd measure_temp').readline()
    return(temp.replace("temp=","").replace("'C\n",""))

def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

#client.on_log = on_log

client.username_pw_set(USER, PASS)
client.connect(HOST, PORT)

while True:
    temp = measure_temp()
    client.publish(TOPIC, temp)
    time.sleep(2)

