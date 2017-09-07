#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lcd import *  
import smbus
import time
import sys
from datetime import datetime

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

lcd_init()

try:
    n = datetime.now()
    n = n.strftime('%Y/%m/%d')
    lcd_string(n, LCD_LINE_1)
    while True:
        n = datetime.now()
        n = n.strftime('%H:%M:%S')
        lcd_string(n, LCD_LINE_2)
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    lcd_string(" ", LCD_LINE_1)
    lcd_string(" ", LCD_LINE_2)
    lcd_byte(0x01, 1)
