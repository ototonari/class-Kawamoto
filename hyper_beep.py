#!/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

TRIG=26
ECHO=19

BEEP=5

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BEEP, GPIO.OUT)

def scale(f):
    global BEEP
    p=GPIO.PWM(BEEP, f)
    p.start(50)
    time.sleep(0.5)

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

    scale(d)
    time.sleep(0.5)
