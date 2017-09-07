#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lcd import *  
import RPi.GPIO as GPIO
import dht11
import smbus
import time
import sys
from datetime import datetime

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

lcd_init()

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=26)

text = sys.argv

try:
    while True:
        if text[1] and text[2]:
                lcd_double(text[1], text[2])
        else:
                lcd_double("(^-^)", "mjd!?")
        time.sleep(0.01)

except KeyboardInterrupt:
    pass

finally:
    lcd_string(" ", LCD_LINE_1)
    lcd_string(" ", LCD_LINE_2)
    lcd_byte(0x01, 1)


