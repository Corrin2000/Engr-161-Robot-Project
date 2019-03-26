# wallstop.py
import time
import brickpi3
import grovepi
import math
import mvmt

BP = brickpi3.BrickPi3()

lineLeft = 5
grovepi.pinMode(lineLeft,"INPUT")
lineRight = 6
grovepi.pinMode(lineRight,"INPUT")
hallSensor = 8
grovepi.pinMode(hallSensor,"INPUT")

spd = -24
cSpd = -70
turnNum = 35
rot = 'line'
cargoDropped = 0

try:
    while 1:
        mvmt.move(spd)
        leftValue = grovepi.digitalRead(lineLeft)
        rightValue = grovepi.digitalRead(lineRight)
        hallValue = grovepi.digitalRead(hallSensor)
        motorA = BP.get_motor_encoder(BP.PORT_A)
        
        print("Left = %d Right: %d\nHall: %d"
              % (leftValue, rightValue, hallValue))
        
        if(leftValue == 0 and rightValue == 0 and rot != 'line'):
            rot = 'line'
            mvmt.turnTo(0)            
        elif(leftValue == 1 and rot != 'left'):
            mvmt.turnTo(turnNum)
            rot = 'left'
            mvmt.forwardDist(spd, 2) 
        elif(rightValue == 1 and rot != 'right'):
            mvmt.turnTo(-turnNum)
            rot = 'right'
            mvmt.forwardDist(spd, 2)

        if(hallValue == 0):
            mvmt.cargoDrop()
        elif(cargoDropped == 0):
            BP.set_motor_dps(BP.PORT_D, cSpd * mvmt.pwrDPSFactor)
            pass
        
        time.sleep(0.1)
except IOError as error:
    print(error)
except TypeError as error:
    print(error)
except KeyboardInterrupt:
    print("You pressed ctrl+C...")
    #mvmt.cargoDrop()
mvmt.move(0)

BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))

BP.reset_all()
