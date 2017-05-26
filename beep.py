import RPi.GPIO as GPIO
import time
PIN=26

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT)

while True:
    GPIO.output(PIN,GPIO.HIGH)
    time.sleep(0.005)
    GPIO.output(PIN,GPIO.LOW)
    time.sleep(0.005)
