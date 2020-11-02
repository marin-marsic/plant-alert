#!/usr/bin/env python3
"""Demo file showing how to use the miflora library."""

import argparse
import logging
import re
import sys
import requests 

from btlewrap import BluepyBackend, GatttoolBackend, PygattBackend, available_backends

from config import *

from miflora import miflora_scanner
from miflora.miflora_poller import (
    MI_BATTERY,
    MI_CONDUCTIVITY,
    MI_LIGHT,
    MI_MOISTURE,
    MI_TEMPERATURE,
    MiFloraPoller,
)

emojiAlert = '\U000026A0'
emojiOk = '\U0001F49A'

def getEmoticon(positive):
    if positive:
        return emojiOk
    return emojiAlert

def poll(mac):
    """Poll data from the sensor."""
    poller = MiFloraPoller(mac, GatttoolBackend)
    print("Getting data from Mi Flora")
    print(f"FW: {poller.firmware_version()}")
    print(f"Name: {poller.name()}")
    
    buffer = poller.name() + "\n"
    
    temperatureVal = poller.parameter_value(MI_TEMPERATURE)
    temperatureOk = temperatureVal >= temperature[0] and temperatureVal <= temperature[1]
    buffer += getEmoticon(temperatureOk) + " Temperature: {}°C\n".format(temperatureVal, temperatureOk)
    
    moistureVal = poller.parameter_value(MI_MOISTURE)
    moistureOk = moistureVal >= moisture[0] and moistureVal <= moisture[1]
    buffer += getEmoticon(temperatureOk) + " Moisture: {}%\n".format(moistureVal, moistureOk)
    
    lightVal = poller.parameter_value(MI_LIGHT)
    lightOk = lightVal >= light[0] and lightVal <= light[1]
    buffer += getEmoticon(lightOk) + " Light: {}lux\n".format(lightVal, lightOk)
    
    fertilityVal = poller.parameter_value(MI_CONDUCTIVITY)
    fertilityOk = fertilityVal >= fertility[0] and fertilityVal <= fertility[1]
    buffer += getEmoticon(fertilityOk) + " Fertility: {}uS/cm\n".format(fertilityVal, fertilityOk)
    
    batteryVal = poller.parameter_value(MI_BATTERY)
    batteryOk = batteryVal > battery
    buffer += getEmoticon(batteryOk) + " Battery: {}%\n".format(batteryVal, batteryOk)
    
    print(buffer)
    
    ""
   
    # Making a POST request 
    r = requests.post(webhookUrl, data ={'value1':buffer}) 
    

for mac in macAddresses:
    poll(mac)
