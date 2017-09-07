#!/usr/bin/python
# -*- coding: utf-8; -*-

import RPi.GPIO as GPIO
import time
PIN=22

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN,GPIO.OUT)
    GPIO.setwarnings(False)

    while True:
        GPIO.output(PIN,GPIO.HIGH)
        time.sleep(10)
except:
    pass
GPIO.output(PIN, GPIO.LOW)
GPIO.cleanup()
