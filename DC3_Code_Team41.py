import time
import brickpi3
import grovepi
import mvmt

BP = brickpi3.BrickPi3()
ultrasonic_sensor_port = 4 # assign ultrasonic sensor port to D4
line_finder = 8
grovepi.pinMode(line_finder,"INPUT")
lightRight = 2
grovepi.pinMode(lightRight, 'INPUT')
angle = 0
spd = 9
turnSpd = 15
turnDist = 3


def casterTurn(dir):
    timer = 0
    try:
        while timer < 4:
            if(dir == 'left'):
                print('LEFT\n\n\n')
                BP.set_motor_power(BP.PORT_B,turnSpd)
                BP.set_motor_power(BP.PORT_C,-turnSpd)
            elif(dir == 'right'):
                print('RIGHT\n\n\n')
                BP.set_motor_power(BP.PORT_B,-turnSpd)
                BP.set_motor_power(BP.PORT_C,turnSpd)
            timer += 1
            time.sleep(.1)
    except IOError as error:
        print(error)
    except TypeError as error:
        print(error)
    except KeyboardInterrupt:
        print("You pressed ctrl+C...")
    
    mvmt.forwardDist(turnDist, 13)

# Main logic    
try:
    while True:
        UsSensor = grovepi.ultrasonicRead(ultrasonic_sensor_port)
        print('loop', spd, UsSensor)
        mvmt.move(-spd)
        if(UsSensor > 35):
            spd = 13
        elif(UsSensor < 35 and UsSensor > 15):
            spd = 7
        elif(UsSensor < 15):
            spd = 0

        left = grovepi.digitalRead(line_finder)
        right = grovepi.analogRead(lightRight)
        
        print('left:', left, 'right:', right)
        if(left == 1):
            casterTurn('left')
        elif(right < 80):
            casterTurn('right')
        time.sleep(.1)

except IOError as error:
    print(error)
except TypeError as error:
    print(error)
except KeyboardInterrupt:
    print("You pressed ctrl+C...")

BP.reset_all()
