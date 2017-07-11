#!/usr/bin/env python

from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.start_preview()

sleep(2)
for filename in camera.capture_continuous('img{counter:03d}.jpg'):
    print('Captured %s' % filename)
    sleep(0.1)
