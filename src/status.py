#!/usr/bin/env python3

from config import *
from db import *
from datetime import datetime

emojiAlert = '\U000026A0'
emojiOk = '\U0001F49A'

def getEmoticon(positive):
    if positive:
        return emojiOk
    return emojiAlert

def checkValue(key, valRange, requireAll):
    dbValues = getList(key, mac)
    valOk = True if requireAll else False
    for dbVal in dbValues:
        if (requireAll):
            if (dbVal < valRange[0] or dbVal > valRange[1]):
                valOk = False
            elif (dbVal >= valRange[0] and dbVal <= valRange[1]):
                valOk = True
                
    return valOk

def poll(mac):
    
    if (getLastUpdate(mac) > 0):
        buffer = ""
        temperatureVal = getTemperatures(mac)[-1]
        temperatureOk = checkValue('temperature', temperature, True)
        buffer += getEmoticon(temperatureOk) + " Temperature: {}°C\n".format(temperatureVal, temperatureOk)
    
        moistureVal = getMoistures(mac)[-1]
        moistureOk = checkValue('moisture', moisture, True)
        buffer += getEmoticon(temperatureOk) + " Moisture: {}%\n".format(moistureVal, moistureOk)
    
        lightVal = getLights(mac)[-1]
        lightOk = checkValue('light', light, False)
        buffer += getEmoticon(lightOk) + " Light: {}lux\n".format(lightVal, lightOk)
    
        fertilityVal = getFertilities(mac)[-1]
        fertilityOk = checkValue('fertility', fertility, True)
        buffer += getEmoticon(fertilityOk) + " Fertility: {}uS/cm\n".format(fertilityVal, fertilityOk)
    
        batteryVal = getBattery(mac)
        batteryOk = batteryVal > battery
        buffer += getEmoticon(batteryOk) + " Battery: {}%\n".format(batteryVal, batteryOk)
    
        buffer += "Updated at: " + datetime.fromtimestamp(getLastUpdate(mac)).strftime("%d/%m/%Y %H:%M")
    
        print(buffer)


for mac in macAddresses:
    poll(mac)
    
db.dump()

