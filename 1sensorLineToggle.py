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

light_cutoff = 100 #UPDATE THIS
spd = -17
turnNum = 35
toggle = 0
onLine = 1

try:
    while 1:
        mvmt.move(spd)
        light_value = grovepi.analogRead(light_sensor)
        motorA = BP.get_motor_encoder(BP.PORT_A)
        
        print("light_value = %d onLine: %d" % (light_value, onLine))
        
        if(light_value > light_cutoff and onLine == 1):
            onLine = 0
            print('toggle: %d' % toggle)
            if(toggle == 1):
                mvmt.turnTo(-turnNum)
                toggle = 0
            elif(toggle == 0):
                mvmt.turnTo(turnNum)
                toggle = 1
        elif(light_value < light_cutoff and onLine == 0):
            mvmt.turnTo(0)
            onLine = 1
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
