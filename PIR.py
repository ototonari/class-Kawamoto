#!/usr/bin/python
# -*- coding: utf-8; -*-
#PIRセンサのデータを取得する

import RPi.GPIO as GPIO
import time
PIN=21
FLAG=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.IN)

#ピンの入力を一定時間毎に監視し、その状態を出力する
while True:
    pirValue = GPIO.input(PIN)
    if ( pirValue == True ):
        print "PIR = ON"
    else:
        print "PIR = OFF"

    time.sleep(0.1)
