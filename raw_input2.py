#/usr/bin/python
#coding:UTF-8
import RPi.GPIO as GPIO
import time

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

#    getch = _Getch()
#    x = getch()
#
#    if (int(x) == 1):
#        print "\n"
#        print 'correct'
#        print x
#    else:
#        print "\n"
#        print 'wrong'
#        print x



#			time.sleep(1)




PIN=24
QIN=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT)
GPIO.setup(QIN,GPIO.OUT)
p=GPIO.PWM(PIN,50)
q=GPIO.PWM(QIN,50)
p.start(5)
q.start(5)
time.sleep(1)
row = 5
col = 5
val = 0.1

def direction(key):
	global row
	global col
	if x == "w" and row > 2:
		row -= val
	elif x == "s" and row < 9:
		row += val
	elif x == "n":
		row = 5
		col = 5
	elif x == "a" and col < 9:
		col += val
	elif x == "d" and col > 2:
		col -= val
	elif x == "z":
		print("DONE.")
		exit()
	p.start(row)
	q.start(col)


try:


	while True:
		getch = _Getch()
		x = getch()
		direction(x)

except KeyboardInterrupt:
	p = GPIO.PWM(PIN,50)
	q = GPIO.PWM(QIN,50)
	p.start(5)
	q.start(5)
	time.sleep(1)
	GPIO.cleanup()
