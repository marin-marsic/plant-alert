#!/usr/bin/env python3
"""Demo file showing how to use the miflora library."""

import argparse
import logging
import re
import sys
import requests
from datetime import datetime
from util import *

from btlewrap import BluepyBackend, GatttoolBackend, PygattBackend, available_backends

from config import *
from db import *

from miflora import miflora_scanner
from miflora.miflora_poller import (
    MI_BATTERY,
    MI_CONDUCTIVITY,
    MI_LIGHT,
    MI_MOISTURE,
    MI_TEMPERATURE,
    MiFloraPoller,
)

def poll(mac):
    """Poll data from the sensor."""
    poller = MiFloraPoller(mac, GatttoolBackend)
    print("Getting data from Mi Flora")
    print(f"FW: {poller.firmware_version()}")
    print(f"Name: {poller.name()}")
    
    buffer = poller.name() + "\n"
    
    temperatureVal = poller.parameter_value(MI_TEMPERATURE)
    insertTemperature(temperatureVal, mac)
    temperatureOk = checkValue(getList('temperature', mac), temperature, True)
    buffer += getEmoticon(temperatureOk) + " Temperature: {}°C\n".format(temperatureVal, temperatureOk)
    
    moistureVal = poller.parameter_value(MI_MOISTURE)
    insertMoisture(moistureVal, mac)
    moistureOk = checkValue(getList('moisture', mac), moisture, True)
    buffer += getEmoticon(moistureOk) + " Moisture: {}%\n".format(moistureVal, moistureOk)
    
    lightVal = poller.parameter_value(MI_LIGHT)
    insertLight(lightVal, mac)
    lightOk = checkValue(getList('light', mac), light, False)
    buffer += getEmoticon(lightOk) + " Light: {}lux\n".format(lightVal, lightOk)
    
    fertilityVal = poller.parameter_value(MI_CONDUCTIVITY)
    insertFertility(fertilityVal, mac)
    fertilityOk = checkValue(getList('fertility', mac), fertility, True)
    buffer += getEmoticon(fertilityOk) + " Fertility: {}uS/cm\n".format(fertilityVal, fertilityOk)
    
    batteryVal = poller.parameter_value(MI_BATTERY)
    insertBattery(batteryVal, mac)
    batteryOk = batteryVal > battery
    buffer += getEmoticon(batteryOk) + " Battery: {}%\n".format(batteryVal, batteryOk)
    
    buffer += "Updated at: " + datetime.now().strftime("%d/%m/%Y %H:%M")
    
    print(buffer)
    
    ""
   
    # Making a POST request 
    r = requests.post(webhookUrl, data = {'value1':buffer})


for mac in macAddresses:
    reset(mac)
    lastUpdate = getLastUpdate(mac)
    if (lastUpdate + 3600 < datetime.now().timestamp()):
        poll(mac)
        insertLastUpdate(datetime.now().timestamp(), mac)
    
db.dump()
