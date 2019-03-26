#!/usr/bin/env python
#
# GrovePi example for using the Grove Hall Sensor (http://wiki.seeedstudio.com/Grove-Hall_Sensor/)
#
# The GrovePi connects the Raspberry Pi and Grove sensors. You can learn more about GrovePi here: http://www.dexterindustries.com/grovepi
#
# Have a question about this example? Ask a TA.
#
# Custom example made by the ENGR 16X teaching team, 2018
#

import time
import grovepi

# Connect the Grove Hall Sensor to digital port D2
# VOUT,NC,VCC,GND

hall_port = 2

grovepi.pinMode(hall_port,"INPUT")

while True:
  try:
    value = grovepi.digitalRead(hall_port)
    print(value)
    time.sleep(0.1)
    
  except IOError:
    print("Error")
