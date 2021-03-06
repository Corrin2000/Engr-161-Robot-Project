# Program provides feedback control based on motor encoder readings
# Developed for in class activity
# ENGR 162, Spring 2018

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.


# initialization
# Tuning parameters
KP = 1.0 # proportional control gain
KI = 1.0 # integral control gain
KD = 0.0 # derivative control gain

dT = 0.02 # time step

target_pos = -123
targetC = -16

current_pos = 0
currentC = 0

P = 0
I = 0
D = 0
PC = 0
DC = 0
IC = 0
e_prev = 0
eC_prev = 0

# --------------------------------
# Hardware initialization
# --------------------------------
BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A) )
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)
BP.set_motor_limits(BP.PORT_A, power=50, dps=200)
# --------------------------------
# ---------------------------------------------------------
# Control loop -- run infinitely until a keyboard interrupt
# ---------------------------------------------------------
try:
    while True:
        sig = BP.get_sensor(BP.PORT_1)
        # get current position
        current_pos = BP.get_motor_encoder(BP.PORT_B)
        #print("current position: " + str(current_pos) )
        e = target_pos - current_pos # error
        print("error of B is " + str(e))

        # set up P,I,D, terms for control inputs
        P = KP * e
        I += KI * e * dT/2
        D = KD * (e - e_prev)/ dT

        # control input for motor
        power_in = P + I + D
        BP.set_motor_power(BP.PORT_B, power_in)
        # save error for this step; needed for D
        e_prev = e

        currentC = BP.get_motor_encoder(BP.PORT_C)
        eC = targetC - currentC # error
        print("error of C is " + str(eC))
        PC = KP * eC
        IC += KI * eC * dT/2
        DC = KD * (eC - eC_prev)/ dT
        powerC = PC + IC + DC
        BP.set_motor_power(BP.PORT_C, powerC)
        eC_prev = eC

        
        time.sleep(dT)

# ---------------------------------------------------------------------
# If a problem occurse with the while or an interrupt from the keyboard
# ---------------------------------------------------------------------
except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    print('You pressed ctrl+c..')
    BP.set_motor_power(BP.PORT_B, 0)
    BP.set_motor_power(BP.PORT_C, 0) 
    BP.reset_all()  
