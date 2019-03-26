# wallstop.py
import time
import brickpi3
import grovepi
import math
import mvmt

BP = brickpi3.BrickPi3()

lightLeft = 0
lightRight = 1
turned = 0
sensorNum = 240
turnNum = 35
spd = -7
timer = 0

grovepi.pinMode(lightLeft, 'INPUT')
grovepi.pinMode(lightRight, 'INPUT')

try:
    while 1:
        sensorLeft = grovepi.analogRead(lightLeft)
        sensorRight = grovepi.analogRead(lightRight)

        mvmt.move(spd)
        
        print('timer: %d left: %d right %d' % (timer, sensorLeft, sensorRight))
        if(sensorLeft < (sensorNum) and sensorRight < (sensorNum)
                    and turned == 1 and timer > 20):
            mvmt.move(0)
            print('center')
            mvmt.center()
            turned = 0
        elif(sensorRight > sensorNum and turned == 0):
            mvmt.move(0)
            print('right')
            turned = 1
            timer = 0
            mvmt.turn(turnNum)
        elif(sensorLeft > sensorNum and turned == 0):
            mvmt.move(0)
            print('left')
            turned  = 1
            timer = 0
            mvmt.turn(-turnNum)

        timer += 1
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
