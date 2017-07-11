#!/usr/bin/python
# coding: utf-8

import os
import cgi
import RPi.GPIO as GPIO
import time
import threading
from datetime import datetime
from picamera import PiCamera

PIN=24
QIN=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT)
GPIO.setup(QIN,GPIO.OUT)

fs = cgi.FieldStorage()
txt = fs.getfirst('text', '')

print("Content-Type: text/html;charset=utf-8")
print("")

print """
<TITLE>CGI script output</TITLE>
<H1>This is my first CGI script</H1>
<p>Hello,world!</p>

<form action="hello.py" method="POST">
<input type="text" name="keyword" value="">
<input type="text" name="spy" value="">
<input type="submit" value="button">
"""

print "<p>value:", fs["keyword"].value, "\n"
print "<p>value:", fs["spy"].value, "\n"

