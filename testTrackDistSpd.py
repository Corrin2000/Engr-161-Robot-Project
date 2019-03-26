# wallstop.py
import time
import brickpi3
import grovepi
import math
import mvmt

BP = brickpi3.BrickPi3()

#INPUT VALUES
spd = 20 #input the target speed in cm/s, default 25, max 67
dist = 400 #input the target distance, default 275 cm

mvmt.forwardDist(spd, dist)


BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))

BP.reset_all()
