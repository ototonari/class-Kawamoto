# coding: utf-8
import RPi.GPIO as GPIO
import time
GPIO.cleanup()
PIN=26
SWICH=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
GPIO.setup(SWICH, GPIO.IN)
def scale(f):
    global PIN
    p=GPIO.PWM(PIN,f)
    p.start(50)
    time.sleep(0.5)

soundlist = [261, 293, 329, 349, 392, 440, 493, 523, 587, 659, 698, 783, 880, 987]
i = (x for x in soundlist)
while True:
    sw = GPIO.input(SWICH)
    if sw == True:
        
        scale(next(i))
    time.sleep(0.1)
