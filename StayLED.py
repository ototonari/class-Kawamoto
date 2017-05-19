#!/usr/python
import RPi.GPIO as GPIO 
from time import sleep

def my_callback(channel):
    global ledstate
    if channel == 21:
        ledstate = not ledstate
        GPIO.output(20, ledstate)

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.IN)

GPIO.add_event_detect(21, GPIO.RISING, callback=my_callback, bouncetime=200)

ledstate = GPIO.LOW

try:
    while True:
        sleep(0.01)

except KeyboardInterrupt: 
    pass

GPIO.cleanup()
