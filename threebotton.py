#!/bin/python

import RPi.GPIO as GPIO
from datetime import datetime, timedelta
import os
import time

cmd="/home/admin/Desktop/IoT/echo.sh"
PIN=21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.IN)

while True:
    sw = GPIO.input(PIN)
    starttime = datetime.now()
    if sw == True:
        while sw:
            sw = GPIO.input(PIN)
            n=datetime.now()
            if n > starttime + timedelta(seconds=3):
                os.system(cmd)
            time.sleep(0.2)
    time.sleep(0.2)
