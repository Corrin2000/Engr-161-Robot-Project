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
BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.CUSTOM, [(BP.SENSOR_CUSTOM.PIN1_ADC)])


spd = -35
cSpd = -70
turnNum = 40
rot = 'line'
cargoDropped = 0
hallMax = 2080
hallMin = 2020
beaconCount = 0
onBeacon = 0
targetBeacon = 3 #UPDATE
seekingDrop = 0
finished = 0

try:
    while finished == 0:
        leftValue = grovepi.digitalRead(lineLeft)
        rightValue = grovepi.digitalRead(lineRight)
        hallValue = BP.get_sensor(BP.PORT_2)[0]
        motorA = BP.get_motor_encoder(BP.PORT_A)
        
        print("Left = %d Right: %d Hall: %d"
              % (leftValue, rightValue, hallValue))
        
        mvmt.move(spd)
        if(seekingDrop == 0):
            mvmt.rotActive(leftValue, rightValue)
        elif(seekingDrop == 1):
            mvmt.rotSeeking(leftValue)
        
        if(cargoDropped == 0):
            if((hallValue > hallMax or hallValue < hallMin) and onBeacon == 0):
                beaconCount += 1
                onBeacon = 1
            elif(beaconCount == targetBeacon - 1):
                seekingDrop = 1
            elif(beaconCount == targetBeacon):
                mvmt.move(0)
                mvmt.forwardSeeking(spd, 25, leftValue, rightValue)
                mvmt.cargoDrop()
                cargoDropped = 1
                seekingDrop = 0
            elif(hallMin < hallValue < hallMax):
                onBeacon = 0
                BP.set_motor_dps(BP.PORT_D, -50)
        elif(beaconCount == targetBeacon + 1):
            finished = 1
        
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
