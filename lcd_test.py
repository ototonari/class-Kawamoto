#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lcd import *  
import smbus
import time
import sys

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

lcd_init()

try:
    p = ""
    if sys.argv[1]:
        p = sys.argv[1]
    lcd_string(p, LCD_LINE_1)

finally:
    lcd_byte(0x01, 1)
