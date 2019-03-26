# Program provides feedback control based on motor encoder readings
# Developed for in class activity
# ENGR 162, Spring 2018

import time     # import the time library for the sleep function
#import brickpi3 # import the BrickPi3 drivers
import grovepi
import BrickPi as BP
BP.BrickPiSetup()

BP.MotorEnable[PORT_B] = 1
BP.MotorEnable[PORT_C] = 1


#BP = BrickPi.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
us_port = 5


# initialization
# Tuning parameters
KP = 1.0 # proportional control gain
KI = 2.0 # integral control gain
KD = 0.0 # derivative control gain

dT = 0.02 # time step

targetB = -123
targetC = -16

currentB = 0
currentC = 0

PB = 0
IB = 0
DB = 0
PC = 0
DC = 0
IC = 0
eB_prev = 0
eC_prev = 0

# --------------------------------
# Hardware initialization
# --------------------------------

'''
BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A) )
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)
BP.set_motor_limits(BP.PORT_A, power=50, dps=200)
'''

# ---------------------------------------------------------
# Control loop -- run infinitely until a keyboard interrupt
# ---------------------------------------------------------
try:
    while True:
        '''
        US = grovepi.digitalRead(us_port)
        print('Ultrasonic is ' + str(US))
        
        current_pos = BP.get_motor_encoder(BP.PORT_B)
        #print("current position: " + str(current_pos) )
        e = targetB - currentB # error
        print("error of B is " + str(e))

        # set up P,I,D, terms for control inputs
        PB = KP * eB
        IB += KI * eB * dT/2
        DB = KD * (eB - eB_prev)/ dT

        # control input for motor
        powerB = PB + IB + DB
        BP.set_motor_power(BP.PORT_B, powerB)
        # save error for this step; needed for D
        eB_prev = eB

        currentC = BP.get_motor_encoder(BP.PORT_C)
        eC = targetC - currentC # error
        print("error of C is " + str(eC))
        PC = KP * eC
        IC += KI * eC * dT/2
        DC = KD * (eC - eC_prev)/ dT
        powerC = PC + IC + DC
        BP.set_motor_power(BP.PORT_C, powerC)
        eC_prev = eC

        '''
        
        BP.MotorSpeed[[PORT_B,PORT_C]] = 20
        time.sleep(dT)

# ---------------------------------------------------------------------
# If a problem occurse with the while or an interrupt from the keyboard
# ---------------------------------------------------------------------
except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    print('You pressed ctrl+c..')
    BP.MotorSpeed[[PORT_B,PORT_C]] = 0
    #BP.reset_all()  
