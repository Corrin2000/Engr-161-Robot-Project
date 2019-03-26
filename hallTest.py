#!/usr/bin/env python
# Jaikrishna
# Initial Date: June 24, 2013
# Last Updated: June 24, 2013
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)
#
# http://www.dexterindustries.com/
# This code is for testing the BrickPi with any Analog sensor

import brickpi3
import time

BP = brickpi3.BrickPi3()
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.CUSTOM, [(BP.SENSOR_CUSTOM.PIN1_ADC)])

try:
    while True:
        hallValue = BP.get_sensor(BP.PORT_3)[0]
        print('hallValue: %d' % hallValue)
        time.sleep(.1)
except KeyboardInterrupt:
    print('you pressed ctrl+c...')
    BP.reset_all()


