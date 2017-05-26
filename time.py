#!/bin/python

from datetime import datetime, timedelta
import time

starttime = datetime.now()
while True:
    n=datetime.now()
    print n.strftime("%x %X")
    if n > starttime + timedelta(seconds=3):
        print "3s gome."
    time.sleep(1)
