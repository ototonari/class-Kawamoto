#!/usr/bin/python
# -*- coding: utf-8; -*-
#
#

import RPi.GPIO as GPIO
import time
INPIN=21
OUTPIN=20
FLAG=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(OUTPIN,GPIO.OUT)
GPIO.setup(INPIN,GPIO.IN)

while True:
    sw = GPIO.input(INPIN)
    if sw == True:
        GPIO.output(OUTPIN,GPIO.HIGH)
        print "ON"
    else:
        GPIO.output(OUTPIN,GPIO.LOW)
        print "OFF"
    time.sleep(0.1)

GPIO.cleanup()
