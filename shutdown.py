#!/usr/bin/python 
# coding:utf-8 
import time
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
 
#GPIO18pinを入力モードとし、pull up設定とします 
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_UP)
 
while True:
    GPIO.wait_for_edge(21, GPIO.FALLING)
    print("割り込みOK!")
 
GPIO.cleanup()
