import time
import brickpi3
import grovepi

BP = brickpi3.BrickPi3()
ultrasonic_sensor_port = 4 # assign ultrasonic sensor port to D4
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)  # Configure port 1 sensor type
spd = 8
timer = 0
   
# Before touch sensor is pressed, your program will be stuck in this loop
print("Press touch sensor on port 1 to run motors")
value = 0
while not value:
    try:
        value = BP.get_sensor(BP.PORT_1)
    except brickpi3.SensorError:
        value = 0
print("Starting...")

# Main logic    
try:
    while True:
        #PUT YOUR LOGIC HERE
        #this infinite loop can be interrupted by ctrl+c a.k.a. keyboardInterrupt      
        BP.set_motor_power(BP.PORT_B+BP.PORT_C,spd)
        if(grovepi.ultrasonicRead(ultrasonic_sensor_port) > 35):
            spd += 1
        elif(20 < grovepi.ultrasonicRead(ultrasonic_sensor_port) < 35):
            spd -= 1
        elif(grovepi.ultrasonicRead(ultrasonic_sensor_port) < 20):
            break

        time.sleep(.2) # hold each loop/iteration for .2 seconds

except IOError as error:
    print(error)
except TypeError as error:
    print(error)
except KeyboardInterrupt:
    print("You pressed ctrl+C...")

try:
    while timer < 30:
        BP.set_motor_power(BP.PORT_B,1)
        BP.set_motor_power(BP.PORT_C,6)

        
        timer +=1
        time.sleep(.2) # hold each loop/iteration for .2 seconds

except IOError as error:
    print(error)
except TypeError as error:
    print(error)
except KeyboardInterrupt:
    print("You pressed ctrl+C...")
BP.set_motor_power(BP.PORT_C+BP.PORT_B,0)

# use reset_all() to return all motors and sensors to resting states
BP.reset_all()
