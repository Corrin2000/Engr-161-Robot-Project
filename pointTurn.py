# Program provides feedback control based on motor encoder readings
# Developed for in class activity
# ENGR 162, Spring 2018

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers
import grovepi

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

angle = 20
spd = 20

BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))

try:
    while True:
        BP.set_motor_power(BP.PORT_B, -spd)
        BP.set_motor_power(BP.PORT_C, spd)
        
        # save error for this step; needed for D

        time.sleep(dT)

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    print('You pressed ctrl+c..')
    BP.set_motor_power(BP.PORT_B+BP.PORT_C, 0)
    BP.reset_all()  
