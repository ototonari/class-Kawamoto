import RPi.GPIO as GPIO
import time
PIN=27

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT)
p=GPIO.PWM(PIN,200)
while True:
    p.start(50)
    time.sleep(3)
    p.stop
    time.sleep(3)
