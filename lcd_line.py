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

try:
    while True:
        result = instance.read()
        if result.is_valid():
            lcd_string_line("T:{temp} H:{humid}".format(temp=result.temperature, humid=result.humidity), LCD_LINE_2)
        n = datetime.now()
        n = n.strftime('%H:%M:%S')
        lcd_string_line(n, LCD_LINE_1)
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    lcd_string(" ", LCD_LINE_1)
    lcd_string(" ", LCD_LINE_2)
    lcd_byte(0x01, 1)


