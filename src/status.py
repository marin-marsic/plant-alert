#!/usr/bin/env python3

from config import *
from db import *
from datetime import datetime
from util import *

def poll(mac):
    
    if (getLastUpdate(mac) > 0):
        buffer = ""
        temperatureVal = getTemperatures(mac)[-1]
        temperatureOk = checkValue(getList('temperature', mac), temperature, True)
        buffer += getEmoticon(temperatureOk) + " Temperature: {}°C\n".format(temperatureVal, temperatureOk)
    
        moistureVal = getMoistures(mac)[-1]
        moistureOk = checkValue(getList('moisture', mac), moisture, True)
        buffer += getEmoticon(moistureOk) + " Moisture: {}%\n".format(moistureVal, moistureOk)
    
        lightVal = getLights(mac)[-1]
        lightOk = checkValue(getList('light', mac), light, False)
        buffer += getEmoticon(lightOk) + " Light: {}lux\n".format(lightVal, lightOk)
    
        fertilityVal = getFertilities(mac)[-1]
        fertilityOk = checkValue(getList('fertility', mac), fertility, True)
        buffer += getEmoticon(fertilityOk) + " Fertility: {}uS/cm\n".format(fertilityVal, fertilityOk)
    
        batteryVal = getBattery(mac)
        batteryOk = batteryVal > battery
        buffer += getEmoticon(batteryOk) + " Battery: {}%\n".format(batteryVal, batteryOk)
    
        buffer += "Updated at: " + datetime.fromtimestamp(getLastUpdate(mac)).strftime("%d/%m/%Y %H:%M")
    
        print(buffer)


for mac in macAddresses:
    poll(mac)
    
db.dump()

