import mvmt
import time
import brickpi3
import grovepi

BP = brickpi3.BrickPi3()

try:
    while 1:
        BP.set_motor_power(BP.PORT_D, 100)
        time.sleep(0.1)
except IOError as error:
    print(error)
except TypeError as error:
    print(error)
except KeyboardInterrupt:
    print("You pressed ctrl+C...")
BP.set_motor_power(BP.PORT_D,0)
BP.reset_all()
