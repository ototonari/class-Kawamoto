#!/usr/bin/python
# -*- coding: utf-8; -*-
#
#

import RPi.GPIO as GPIO
import time
GREEN=21
YELLOW=20
RED=26

GPIO.setmode(GPIO.BCM)

GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)

GPIO.output(GREEN,GPIO.HIGH)
time.sleep(5)
GPIO.output(GREEN,GPIO.LOW)
GPIO.output(YELLOW,GPIO.HIGH)
time.sleep(3)
GPIO.output(YELLOW,GPIO.LOW)
GPIO.output(RED,GPIO.HIGH)
time.sleep(5)
GPIO.output(RED,GPIO.LOW)





GPIO.cleanup()
