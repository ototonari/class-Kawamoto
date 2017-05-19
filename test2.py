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

def my_callback(FLAG):
    if FLAG == 0:
        GPIO.output(OUTPIN,GPIO.HIGH)
        FLAG = 1
    elif FLAG == 1:
        GPIO.output(OUTPIN,GPIO,LOW)
        FLAG = 0

GPIO.add_event_detect(INPIN, GPIO.RISING, callback=my_callback(FLAG), bouncetime=200)

while True:
    time.sleep(0.1)

GPIO.cleanup()
