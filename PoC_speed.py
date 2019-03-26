# wallstop.py
import time
import brickpi3
import grovepi
import math
import turning

BP = brickpi3.BrickPi3()

#INPUT VALUES
inputSpd = 20 #input the target speed in cm/s, default 25, max 67

spd = inputSpd * 3 / 2 #Multiply by 3/2 to get cm/s
timer = 0

try:
        while 1:
                print("Loop: %d Motor A: %6d  B: %6d  C: %6d  D: %6d" \
			% (timer, BP.get_motor_encoder(BP.PORT_A), \
				BP.get_motor_encoder(BP.PORT_B), \
				BP.get_motor_encoder(BP.PORT_C), \
				BP.get_motor_encoder(BP.PORT_D)))
                BP.set_motor_power(BP.PORT_C+BP.PORT_B, -spd)
                time.sleep(0.1)
                timer+=1
except IOError as error:
        BP.set_motor_power(BP.PORT_B+BP.PORT_C,0)
        print(error)
except TypeError as error:
        BP.set_motor_power(BP.PORT_B+BP.PORT_C,0)
        print(error)
except KeyboardInterrupt:
        BP.set_motor_power(BP.PORT_B+BP.PORT_C,0)
        print("You pressed ctrl+C...")


BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))

BP.reset_all()
