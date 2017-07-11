#/usr/bin/python
#coding:UTF-8
import RPi.GPIO as GPIO
import time
import threading
from datetime import datetime
from picamera import PiCamera

PIN=24
QIN=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT)
GPIO.setup(QIN,GPIO.OUT)
p=GPIO.PWM(PIN,50)
q=GPIO.PWM(QIN,50)
p.start(5)
q.start(5)
time.sleep(1)

def move():
	p.start(9)
	q.start(9)
	time.sleep(1)
try:
	while True:
		move()
		

except KeyboardInterrupt:
	pass
