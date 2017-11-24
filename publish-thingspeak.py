#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Publish ds1820 temperature data
    to thingspeak
"""
import os 
import time
import sys, signal
import requests
THINGSPEAKAPIKEY = os.environ['THINGSPEAKAPIKEY']

def getTemp():
    """
    get temperature frome sensors
    """
    data = dict()
    file = open('/sys/devices/w1_bus_master1/w1_master_slaves')
    w1_slaves = file.readlines()
    file.close()

    for line in w1_slaves:
        w1_slave = line.split("\n")[0]
        file = open('/sys/bus/w1/devices/' + str(w1_slave) + '/w1_slave')
        filecontent = file.read()
        file.close()

        stringvalue = filecontent.split("\n")[1].split(" ")[9]
        temperature = float(stringvalue[2:]) / 1000
        data.update({w1_slave : temperature})

    return data


def publish(apikey):
    """
    publish temperatures
    """
    payload = {'api_key' : apikey}
    sensor = 1
    result = getTemp()

    for dev, temp in result.items():
        field = "field{0}".format(sensor)
        payload[field] = "{:6.2f}".format(temp)
        sensor += 1

    r = requests.post('https://api.thingspeak.com/update.json', data=payload)
    if r.status_code != 200:
        print(r.text)

if __name__ == "__main__":
    publish(THINGSPEAKAPIKEY) 
