# wallstop.py
import time
import brickpi3
import grovepi
import math
import mvmt

BP = brickpi3.BrickPi3()

line_finder = 6
grovepi.pinMode(line_finder,"INPUT")
light_sensor = 1
grovepi.pinMode(light_sensor,"INPUT")

sensorNum = 80
turnNum = 35
light_cutoff = 200 #UPDATE THIS
spd = -10
turnSpd = 10

try:
    while 1:
        mvmt.move(spd)
        line_value = grovepi.digitalRead(line_finder)
        light_value = grovepi.analogRead(light_sensor)
        motorA = BP.get_motor_encoder(BP.PORT_A)
        
        print("line_value: %d light_value = %d motorA: %d" % (line_value, light_value, motorA))
        
        #if(line_value == 1 and motorA > -turnNum):
        if(light_value > light_cutoff and motorA < turnNum):
            mvmt.turnIncrement('left')
        #elif(line_value == 0 and motorA < turnNum):
        elif(light_value < light_cutoff and motorA > -turnNum):
            mvmt.turnIncrement('right')
        time.sleep(0.1)
except IOError as error:
    print(error)
except TypeError as error:
    print(error)
except KeyboardInterrupt:
    print("You pressed ctrl+C...")
mvmt.move(0)

BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
BP.offset_motor_encoder(BP.PORT_B, BP.get_motor_encoder(BP.PORT_B))
BP.offset_motor_encoder(BP.PORT_C, BP.get_motor_encoder(BP.PORT_C))
BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))

BP.reset_all()
