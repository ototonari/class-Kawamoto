#!/usr/bin/python
# -*- coding: utf-8; -*-
#
#

import RPi.GPIO as GPIO
import time
PIN=5

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT)

GPIO.output(PIN,GPIO.HIGH)

time.sleep(5)

GPIO.output(PIN,GPIO.LOW)


GPIO.cleanup()
