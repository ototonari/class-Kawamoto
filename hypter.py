#!/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

TRIG=26
ECHO=19

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

while True:
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    while GPIO.input(ECHO) == 0:
        now = time.time()
    
    while GPIO.input(ECHO) == 1:
        ref = time.time()

    t = ref - now
    d = t * 17000

    print d
    time.sleep(1)
