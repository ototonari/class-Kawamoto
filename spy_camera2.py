#/usr/bin/python
#coding:UTF-8
import RPi.GPIO as GPIO
import time
import threading
from datetime import datetime
from picamera import PiCamera


class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


PIN=24
QIN=23
SW=5
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT)
GPIO.setup(QIN,GPIO.OUT)
GPIO.setup(SW,GPIO.OUT)
GPIO.output(SW,GPIO.HIGH)
p=GPIO.PWM(PIN,50)
q=GPIO.PWM(QIN,50)
p.start(5)
q.start(5)
time.sleep(1)
row = 5
col = 5
val = 0.2

camera = PiCamera()
camera.resolution = (1024, 768)
camera.vflip = True
camera.hflip = True

print("Ready.")

def direction(key):
	global row
	global col
	global val
	if key == "w" and row > 2:
		row -= val
		move()
	elif key == "s" and row < 9:
		row += val
		move()
	elif key == "n":
		row = 5
		col = 5
		val = 0.2
		move()
	elif key == "a" and col < 9:
		col += val
		move()
	elif key == "d" and col > 2:
		col -= val
		move()
	elif key == "p":
		picture()
	elif key == "+" and val < 0.5:
		val += 0.1
		print(val)
	elif key == "-" and val > 0.1:
		val -= 0.1
		print(val)
	elif key == "z":
		cleanup()
	#time.sleep(0.1)

def picture():
	n = datetime.now()
	np = datetime.strftime(n, "/home/share/%Y-%m-%d-%H:%M:%S.%f.jpg")
	camera.capture(np)
	print("captured.")

def cleanup():
	p.start(5)
	q.start(5)
	time.sleep(1)
        GPIO.output(SW,GPIO.LOW)
	GPIO.cleanup()
	print("DONE.")
	exit()

def move():
	p.start(row)
	q.start(col)
	time.sleep(0.2)

try:
	while True:
		getch = _Getch()
		x = getch()
		direction(x)
		

except KeyboardInterrupt:
	pass
