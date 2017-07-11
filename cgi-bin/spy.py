#!/usr/bin/python
# coding: utf-8

import cgi
import RPi.GPIO as GPIO
import time
from picamera import PiCamera

PIN=24
QIN=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT)
GPIO.setup(QIN,GPIO.OUT)
p=GPIO.PWM(PIN,50)
q=GPIO.PWM(QIN,50)

# PiCamera
#camera = PiCamera()
#camera.resolution = (1024, 768)
#camera.vflip = True
#camera.hflip = True



fs = cgi.FieldStorage()
txt = fs.getfirst('text', '')

key = fs["spy"].value

col = int(fs["col"].value)
row = int(fs["row"].value)

def control(num, dir):
    if dir == "col":
        global col
        col += num
        if col > 9:
            col = 9
        elif col < 2:
            col = 2
    elif dir == "row":
        global row
        row += num
        if row > 9:
            row = 9
        elif row < 2:
            row = 2
    elif dir == "reset":
        global col
        global row
        col = 5
        row = 5

#def picture():
#        fn = "capture.jpg"
#        camera.capture(fn)
#        print("captured.")


if key == "a":
    control(1, "col")
elif key == "w":
    control(-1, "row")
elif key == "s":
    control(1, "row")
elif key == "d":
    control(-1, "col")
elif key == "n":
    control(0, "reset")
#elif key == "p":
#    picture()

p.start(row)
q.start(col)

time.sleep(1)

GPIO.cleanup()

print("Content-Type: text/html;charset=utf-8")
print("")

print()


print """
<TITLE>CGI script output</TITLE>
<H1>This is my first CGI script</H1>
<p>Hello,world!</p>
"""

strings = """

<form action="spy.py" method="POST">
<input type="text" name="col" value="{col}">
<input type="text" name="row" value="{row}">
<input type="submit" name="spy" value="w">
<input type="submit" name="spy" value="s">
<input type="submit" name="spy" value="a">
<input type="submit" name="spy" value="d">
<input type="submit" name="spy" value="n">
<input type="submit" name="spy" value="p">

"""

print(strings.format(col=col, row=row))
print "<p>value:", key

