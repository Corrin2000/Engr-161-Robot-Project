import time
import brickpi3
import grovepi
import math
import mvmt

#CALCULATIONS
BP = brickpi3.BrickPi3()
spd = -70

try:
    while 1:
        BP.set_motor_power(BP.PORT_D, spd)
        time.sleep(0.1)
except IOError as error:
    print(error)
except TypeError as error:
    print(error)
except KeyboardInterrupt:
    print("You pressed ctrl+C...")

for i in range(4):
    BP.set_motor_power(BP.PORT_D, -spd)
    time.sleep(0.1)
        
BP.set_motor_power(BP.PORT_D,0)
BP.reset_all()

BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))
