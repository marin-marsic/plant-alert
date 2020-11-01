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

def poll():
    """Poll data from the sensor."""
    poller = MiFloraPoller(mac, GatttoolBackend)
    print("Getting data from Mi Flora")
    print(f"FW: {poller.firmware_version()}")
    print(f"Name: {poller.name()}")
    
    buffer = ""
    
    temperatureVal = poller.parameter_value(MI_TEMPERATURE)
    temperatureOk = temperatureVal >= temperature[0] and temperatureVal <= temperature[1]
    buffer += "Temperature: {} -> {}\n".format(temperatureVal, temperatureOk)
    
    moistureVal = poller.parameter_value(MI_MOISTURE)
    moistureOk = moistureVal >= moisture[0] and moistureVal <= moisture[1]
    buffer += "Moisture: {} -> {}\n".format(moistureVal, moistureOk)
    
    lightVal = poller.parameter_value(MI_LIGHT)
    lightOk = moistureVal >= light[0] and lightVal <= light[1]
    buffer += "Light: {} -> {}\n".format(lightVal, lightOk)
    
    fertilityVal = poller.parameter_value(MI_CONDUCTIVITY)
    fertilityOk = fertilityVal >= fertility[0] and fertilityVal <= fertility[1]
    buffer += "Fertility: {} -> {}\n".format(fertilityVal, fertilityOk)
    
    batteryVal = poller.parameter_value(MI_BATTERY)
    batteryOk = batteryVal > battery
    buffer += "Battery: {} -> {}\n".format(batteryVal, batteryOk)
    
    print(buffer)

   
    # Making a POST request 
    r = requests.post('https://maker.ifttt.com/trigger/plant-alert/with/key/' + webhookKey, data ={'value1':buffer}) 
    

poll()
