import RPi.GPIO as GPIO
import time

PIN=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.IN)

while True:
    sw = GPIO.input(PIN)
    if sw == True:
        print "sw on"
    else:
        print "sw off"
    time.sleep(0.1)
