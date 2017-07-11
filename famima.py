# coding: utf-8
import RPi.GPIO as GPIO
import time
GPIO.cleanup()
PIN=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
def scale(f,t=0.25):
    global PIN
    p=GPIO.PWM(PIN,f/2)
    p.start(50)
    time.sleep(t)

sl = [291.66, 329.23, 369.99, 440]

scale(698)
scale(587)
scale(440)
scale(587)
scale(659)
scale(880,0.75)
scale(659)
scale(698)
scale(659)
scale(440)
scale(587)
 
