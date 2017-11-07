#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import sys, signal

def signal_handler(signal, frame):
    print("\nprogram exited")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

TOPIC = "pi-temperature"
HOST = "test.mosquitto.org"

def on_connect(client, userdata, flag, rc):
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print("Temperature = ", msg.payload.decode('utf-8'))
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(HOST, 1883, 60)
client.loop_forever()


