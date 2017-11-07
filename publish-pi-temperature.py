#!/usr/bin/env python3

import os 
import time
import paho.mqtt.publish as publish
import sys, signal

def signal_handler(signal, frame):
    print("\nprogram exited")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

TOPIC = "pi-temperature"
HOST = "test.mosquitto.org"

def measure_temp():
    temp = os.popen('vcgencmd measure_temp').readline()
    return(temp.replace("temp=","").replace("'C\n",""))

while True:
    temp = measure_temp()
    publish.single(TOPIC, temp, hostname=HOST)
    time.sleep(2)

