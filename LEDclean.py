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

#GPIO.output(PIN,GPIO.HIG)

GPIO.output(PIN,GPIO.LOW)


GPIO.cleanup()
