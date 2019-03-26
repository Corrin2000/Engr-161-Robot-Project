# wallstop.py
import time
import brickpi3
import grovepi
import math
import mvmt

BP = brickpi3.BrickPi3()

lightLeft = 2
lightRight = 1
sensorNum = 80
turnNum = 35
spd = -10
turned = 0

leftNum = 350
rightNum = 350

grovepi.pinMode(lightLeft, 'INPUT')
grovepi.pinMode(lightRight, 'INPUT')

try:
    while 1:
        sensorLeft = grovepi.analogRead(lightLeft)
        sensorRight = grovepi.analogRead(lightRight)

        mvmt.move(spd)
        
        print('left: %d right %d' % (sensorLeft, sensorRight))
        if(sensorLeft > leftNum and sensorRight > rightNum and turned == 1):
            mvmt.move(0)
            print('CENTER\n')
            mvmt.center()
            turned = 0
        elif(sensorRight < rightNum):
            mvmt.move(0)
            print('RIGHT\n')
            mvmt.turnIncrement('left')
            turned = 1
        elif(sensorLeft < leftNum):
            mvmt.move(0)
            print('LEFT\n')
            mvmt.turnIncrement('right')
            turned = 1

        time.sleep(0.1)
except IOError as error:
    print(error)
except TypeError as error:
    print(error)
except KeyboardInterrupt:
    print("You pressed ctrl+C...")
mvmt.move(0)
BP.reset_all()


BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))

BP.reset_all()
