#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Get id and temperature from all ds18s20 devices connected
to Raspberry Pi
code adapted from www.netzmafia.de
"""

def getTemp():
    data = dict()
    # 1-Wire Slave-Liste lesen
    file = open('/sys/devices/w1_bus_master1/w1_master_slaves')
    w1_slaves = file.readlines()
    file.close()

    # Fuer jeden 1-Wire Slave aktuelle Temperatur ausgeben
    for line in w1_slaves:
        # 1-wire Slave extrahieren
        w1_slave = line.split("\n")[0]
        # 1-wire Slave Datei lesen
        file = open('/sys/bus/w1/devices/' + str(w1_slave) + '/w1_slave')
        filecontent = file.read()
        file.close()

        # Temperaturwerte auslesen und konvertieren
        stringvalue = filecontent.split("\n")[1].split(" ")[9]
        temperature = float(stringvalue[2:]) / 1000
        data.update({w1_slave : temperature})

    return data

if __name__ == "__main__":
    result = getTemp()
    for dev, temp in result.items():
        print(str(dev) + ': %6.2f °C' % temp)

