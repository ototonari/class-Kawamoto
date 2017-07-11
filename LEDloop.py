#!/usr/bin/python
# -*- coding: utf-8; -*-
#
#

import RPi.GPIO as GPIO
import time
PIN=21
Ti=0.5
GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN,GPIO.OUT)
while True:

	GPIO.output(PIN,GPIO.HIGH)
	time.sleep(Ti)
	GPIO.output(PIN,GPIO.LOW)
	time.sleep(Ti)
	Ti -= 0.05

GPIO.output(PIN,GPIO.LOW)
GPIO.cleanup()
