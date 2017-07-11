import RPi.GPIO as GPIO
import time
PIN=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

p=GPIO.PWM(PIN,50)
p.start(7.5)
time.sleep(1)
GPIO.cleanup()
