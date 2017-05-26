#!/bin/python

import RPi.GPIO as GPIO
from datetime import datetime, timedelta
import os
import time

cmd="/home/admin/Desktop/IoT/echo.sh"
PIN=21
COUNT=0

starttime = datetime.now()

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.IN)

while True:
    sw = GPIO.input(PIN)
    
    n=datetime.now()
    
    if sw == True:
        COUNT += 1
    
    if COUNT > 3:
        os.system(cmd)

    if n > starttime + timedelta(seconds=3):
        COUNT = 0
        starttime = datetime.now()
        print "reset"
        
    time.sleep(0.1)
