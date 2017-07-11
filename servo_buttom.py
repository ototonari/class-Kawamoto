import RPi.GPIO as GPIO
import time
CON=26
LEFT=21
CENTER=20
RIGHT=16
DIRECTION=7.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(CON, GPIO.OUT)
GPIO.setup(LEFT, GPIO.IN)
GPIO.setup(CENTER, GPIO.IN)
GPIO.setup(RIGHT, GPIO.IN)


def my_callback(channel):
    if channel == 21:
        global DIRECTION
        #DIRECTION -= 0.1
        DIRECTION = 5
    elif channel == 20:
        global DIRECTION
        DIRECTION =7.5
    elif channel == 16:
        global DIRECTION
        #DIRECTION += 0.1
        DIRECTION = 10


GPIO.add_event_detect(LEFT, GPIO.RISING, callback=my_callback)
GPIO.add_event_detect(CENTER, GPIO.RISING, callback=my_callback)
GPIO.add_event_detect(RIGHT, GPIO.RISING, callback=my_callback)

p=GPIO.PWM(CON,50)

try:
    while True:
        p.start(DIRECTION)
        time.sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
