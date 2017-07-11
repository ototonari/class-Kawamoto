import RPi.GPIO as GPIO
import time
PIN=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

p=GPIO.PWM(PIN,50)
p.start(10)
time.sleep(1)
GPIO.cleanup()
