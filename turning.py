import time
import brickpi3
import grovepi
import math

BP = brickpi3.BrickPi3()
rotation = 0
BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
print(BP.get_motor_encoder(BP.PORT_A))

def turnLeft(rotation):
    timer = 1
    motorA = rotation + BP.get_motor_encoder(BP.PORT_A)
    try:
        while motorA < 45:
            motorA = rotation + BP.get_motor_encoder(BP.PORT_A)
            print("Loop: %d Motor A: %6d" % (timer, motorA))
            BP.set_motor_power(BP.PORT_A, 10)
            time.sleep(0.1)
            timer+=1
    except IOError as error:
        BP.set_motor_power(BP.PORT_A,0)
        print(error)
    except TypeError as error:
        BP.set_motor_power(BP.PORT_A,0)
        print(error)
    except KeyboardInterrupt:
        BP.set_motor_power(BP.PORT_A,0)
        print("You pressed ctrl+C...")

    BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
    BP.reset_all()
    return (motorA)

def turnRight(rotation):
    timer = 1
    motorA = rotation + BP.get_motor_encoder(BP.PORT_A)
    try:
        while motorA > -45:
            motorA = rotation + BP.get_motor_encoder(BP.PORT_A)
            print("Loop: %d Motor A: %6d" % (timer, motorA))
            BP.set_motor_power(BP.PORT_A, -10)
            time.sleep(0.1)
            timer+=1
    except IOError as error:
        BP.set_motor_power(BP.PORT_A,0)
        print(error)
    except TypeError as error:
        BP.set_motor_power(BP.PORT_A,0)
        print(error)
    except KeyboardInterrupt:
        BP.set_motor_power(BP.PORT_A,0)
        print("You pressed ctrl+C...")

    BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
    BP.reset_all()
    return (motorA)

def center(rotation):
    timer = 1
    motorA = rotation + BP.get_motor_encoder(BP.PORT_A)
    try:
        while motorA < -5 or motorA > 5:
            motorA = rotation + BP.get_motor_encoder(BP.PORT_A)
            print("Loop: %d Motor A: %6d" % (timer, motorA))
            if motorA > 5:
                BP.set_motor_power(BP.PORT_A, -10)
            elif motorA < -5:
                BP.set_motor_power(BP.PORT_A, 10)
            time.sleep(0.1)
            timer+=1
    except IOError as error:
        BP.set_motor_power(BP.PORT_A,0)
        print(error)
    except TypeError as error:
        BP.set_motor_power(BP.PORT_A,0)
        print(error)
    except KeyboardInterrupt:
        BP.set_motor_power(BP.PORT_A,0)
        print("You pressed ctrl+C...")

    BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
    BP.reset_all()
    return (motorA)

rotation = turnRight(rotation)
print(rotation, '  ', BP.get_motor_encoder(BP.PORT_A))
rotation = turnLeft(rotation)
print(rotation, '  ', BP.get_motor_encoder(BP.PORT_A))
rotation = center(rotation)
print(rotation, '  ', BP.get_motor_encoder(BP.PORT_A))

