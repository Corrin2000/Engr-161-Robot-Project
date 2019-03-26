import time
import brickpi3
import grovepi
import math

'''
---IMPORTANT---
for the turn(angle) function, left is positive!!!
Center brings it back to initial rotation (at the start of this execution of the program)
'''

#Ignore these
BP = brickpi3.BrickPi3()
turnSpd = 20
speed = -18
centerVal = 2
turnNum = 35
pwrDPSFactor = 13.3
BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))


def turnTo(angle):
    move(0)
    timer = 0
    motorA = BP.get_motor_encoder(BP.PORT_A)
    if angle < 0:
        try:
            while motorA > angle:
                motorA = BP.get_motor_encoder(BP.PORT_A)
                print("Loop: %d Motor A: %6d" % (timer, motorA))
                BP.set_motor_dps(BP.PORT_A, -turnSpd*pwrDPSFactor)
                time.sleep(0.1)
                timer+=1
        except IOError as error:
            print(error)
        except TypeError as error:
            print(error)
        except KeyboardInterrupt:
            print("You pressed ctrl+C...")
    else:
        try:
            while motorA < angle:
                motorA = BP.get_motor_encoder(BP.PORT_A)
                print("Loop: %d Motor A: %6d" % (timer, motorA))
                BP.set_motor_dps(BP.PORT_A, turnSpd * pwrDPSFactor)
                time.sleep(0.1)
                timer+=1
        except IOError as error:
            print(error)
        except TypeError as error:
            print(error)
        except KeyboardInterrupt:
            print("You pressed ctrl+C...")
    BP.set_motor_power(BP.PORT_A,0)

def center():
    timer = 0
    motorA = BP.get_motor_encoder(BP.PORT_A)
    try:
        while motorA < -centerVal or motorA > centerVal:
            motorA = BP.get_motor_encoder(BP.PORT_A)
            print("Loop: %d Motor A: %6d" % (timer, motorA))
            if motorA > centerVal:
                BP.set_motor_dps(BP.PORT_A, -turnSpd*pwrDPSFactor)
            elif motorA < -centerVal:
                BP.set_motor_dps(BP.PORT_A, turnSpd*pwrDPSFactor)
            time.sleep(0.1)
            timer+=1
    except IOError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyboardInterrupt:
        print("You pressed ctrl+C...")
    BP.set_motor_power(BP.PORT_A,0)

def forwardTimed(spd, loops):
    timer = 0
    try:
        while timer < loops:
                print("Loop: %d Motor A: %6d  B: %6d  C: %6d  D: %6d" \
			% (timer, BP.get_motor_encoder(BP.PORT_A), \
				BP.get_motor_encoder(BP.PORT_B), \
				BP.get_motor_encoder(BP.PORT_C), \
				BP.get_motor_encoder(BP.PORT_D)))
                BP.set_motor_dps(BP.PORT_C+BP.PORT_B, -spd*pwrDPSFactor)
                time.sleep(0.1)
                timer+=1
    except IOError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyboardInterrupt:
        print("You pressed ctrl+C...")
    BP.set_motor_dps(BP.PORT_B+BP.PORT_C,0)
    BP.reset_all()

def forwardDist(spd, dist):
    timer = 0
    try:
        while timer < (dist / abs(spd) * 10):
            print('Loop: %d Travelling...' % timer)
            BP.set_motor_dps(BP.PORT_C+BP.PORT_B, spd*pwrDPSFactor)
            time.sleep(0.1)
            timer+=1
    except IOError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyboardInterrupt:
        print("You pressed ctrl+C...")
    BP.set_motor_dps(BP.PORT_B+BP.PORT_C,0)

def forwardSeeking(spd, dist, left, right):
    timer = 0
    try:
        while timer < (dist / abs(spd) * 10):
            print('Loop: %d Seeking...' % timer)
            BP.set_motor_dps(BP.PORT_C+BP.PORT_B, spd*pwrDPSFactor)
            rotActive(left, right)
            time.sleep(0.1)
            timer+=1
    except IOError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyboardInterrupt:
        print("You pressed ctrl+C...")
    BP.set_motor_dps(BP.PORT_B+BP.PORT_C,0)

def move(spd):
    BP.set_motor_dps(BP.PORT_B+BP.PORT_C,spd*pwrDPSFactor)

def turnIncrement(direction):
    timer = 0
    try:
        while timer < 2:
            if(direction == 'left'):
                print('LEFT')
                BP.set_motor_dps(BP.PORT_A,turnSpd*pwrDPSFactor)
            elif(direction == 'right'):
                print('RIGHT')
                BP.set_motor_dps(BP.PORT_A,-turnSpd*pwrDPSFactor)
            timer += 1
            time.sleep(.1)
    except IOError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyboardInterrupt:
        print("You pressed ctrl+C...")
    BP.set_motor_dps(BP.PORT_A,0)

def cargoDrop():
    move(0)
    time.sleep(0.5)
    for i in range(6):
        BP.set_motor_dps(BP.PORT_D, 100*pwrDPSFactor)
        time.sleep(0.1)            
    BP.set_motor_dps(BP.PORT_D,0)
    time.sleep(0.5)

def rotActive(leftValue, rightValue):
    rot = 'line'
    if(leftValue == 0 and rightValue == 0 and rot != 'line'):
        rot = 'line'
        turnTo(0)            
    elif(leftValue == 1 and rot != 'left'):
        turnTo(turnNum)
        rot = 'left'
        forwardDist(spd, 2) 
    elif(rightValue == 1 and rot != 'right'):
        turnTo(-turnNum)
        rot = 'right'
        forwardDist(spd, 2)

def rotSeeking(leftValue):
    motorA = BP.get_motor_encoder(BP.PORT_A)
    if(leftValue == 1 and motorA < turnNum):
        turnTo(turnNum)
        forwardDist(spd, 2)
    elif(leftValue == 0 and motorA > turnNum):
        turnTo(-turnNum)
        forwardDist(spd, 2)
