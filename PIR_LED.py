#!/usr/bin/python
# -*- coding: utf-8; -*-
#PIRセンサのデータを取得する

import RPi.GPIO as GPIO
import time

INPUTPIN=21
OUTPUTPIN=20
FLAG=0
ledstate = GPIO.HIGH


def my_callback(channel):
    global ledstate
    for i in range(0,5):
        GPIO.output(OUTPUTPIN, ledstate)
        ledstate = not ledstate

GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUTPIN,GPIO.IN)
GPIO.setup(OUTPUTPIN,GPIO.OUT)

GPIO.add_event_detect(INPUTPIN, GPIO.RISING, callback=my_callback, bouncetime=500)



try:
    while True:
        time.sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
