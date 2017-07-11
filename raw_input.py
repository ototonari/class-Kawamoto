#/usr/bin/python
#coding:UTF-8
import RPi.GPIO as GPIO
import time
PIN=23
QIN=24
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT)
GPIO.setup(QIN,GPIO.OUT)
p=GPIO.PWM(PIN,50)
q=GPIO.PWM(QIN,50)
p.start(5)
q.start(5)
time.sleep(1)
row = 5
col = 5

try:


	while True:
		x=raw_input("入力してください:")
		if x == "w":
			p.start(row + 0.5)
			time.sleep(1)
		elif x == "s":
			p.start(row - 0.5)
			time.sleep(1)
		elif x == "n":
			p.start(5)
			q.start(5)
			time.sleep(1)
		elif x == "a":
			q.start(col - 0.5)
			time.sleep(1)
		elif x == "d":
			q.start(col + 0.5)
			time.sleep(1)

except KeyboardInterrupt:
	p = GPIO.PWM(PIN,50)
	q = GPIO.PWM(QIN,50)
	p.start(5)
	q.start(5)
	time.sleep(1)
	GPIO.cleanup()
