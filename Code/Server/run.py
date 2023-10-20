from random import randint
import time
from Motor import *
from Led import *
from Ultrasonic import *
from Servo import *

MIN_DISTANCE = 10  # Minimum distance to trigger object detection
counter = 0
Car = Motor()
ultrasonic = Ultrasonic()
led = Led()
servo = Servo()

# Initial state
state = "Driving"

def move_forward(distance):
    servo.setServoPwm('0',90)
    led.ledIndex(0x10,0,255,0)
    led.ledIndex(0x20,0,255,0)

    Car.setMotorModel(distance*10,distance*10,distance*10,distance*10)
    time.sleep(5)
    led.colorWipe(led.strip, Color(0,0,0))

    
def object_detected():
    return True if ultrasonic.getDistance() > 0
def detected_distance():
    return ultrasonic.getDistance()
def stop():
    led.ledIndex(0x02,255,0,0)
    led.ledIndex(0x04,255,0,0)
    Car.setMotorModel(0,0,0,0)
    time.sleep(5)
    led.colorWipe(led.strip, Color(0,0,0))
    state = "Field of View Examination"
def turn_left()
    Car.setMotorModel(500,0,-500,0)
    time.sleep(1)
def turn_right()
    Car.setMotorModel(-500,0,500,0)
    time.sleep(1)
def scan(direction):
    if direction is "left":
        for i in range(30,90,1)
            servo.setServoPwm('0',i)
            time.sleep(0.01)
    elif direction is "right":
        if direction is "left":
        for i in range(90,150,1)
            servo.setServoPwm('0',i)
            time.sleep(0.01)
    elif direction is "back":
        led.ledIndex(0x02,255,255,0)
   `    led.ledIndex(0x04,255,255,0)
        Car.setMotorModel(distance*-10,distance*-10,distance*-10,distance*-10)
        time.sleep(1)\    
        led.colorWipe(led.strip, Color(0,0,0))

    else:
        stop()

def valid_path_found():
    return True if not object_detected or detected_distance < MIN_DISTANCE else state is "stop"



# Main program loop
while True:
    if state == "Drive":
        # Move the car forward
        if valid_path_found():
            if detected_distance() > 100:
                move_forward(100)
            else:
                move_forward(detected_distance - MIN_DISTANCE) 
        # Check for object detection
        else:
            state = "stop"

    elif state == "Stop":
        # Stop the car
        stop()
        
        state = "Field of View Examination"

    elif state == "Field of View Examination":
        # Rotate the servos to examine the field of view
        determinant = randint(0,1)
        if determinant < 1:
            scan("left")
            if valid_path_found():
                turn_left()
                while counter > 10
                    led.ledIndex(0x10,255,255,0)
                    time.sleep(0.5)
                    led.colorWipe(led.strip, Color(0,0,0))
                    counter = counter +1
                counter = 0
                state = "Drive"
            if state != "Drive":
                scan("right")
                if valid_path_found():
                    turn_right()
                    while counter > 10
                        led.ledIndex(0x20,255,255,0)
                        time.sleep(0.5)
                        led.colorWipe(led.strip, Color(0,0,0))
                        counter = counter +1
                    counter = 0
                    state = "Drive"
                if state != "Drive":
                    scan("back")
                    if valid_path_found():
                        state = "Field of View Examination"
        else:
            scan("right")
            if valid_path_found():
                turn_right()
                while counter > 10
                    led.ledIndex(0x10,255,255,0)
                    time.sleep(0.5)
                    led.colorWipe(led.strip, Color(0,0,0))
                    counter = counter +1
                counter = 0
                state = "Drive"
            if state != "Drive":
                scan("left")
                if valid_path_found():
                    turn_left()
                    while counter > 10
                        led.ledIndex(0x10,255,255,0)
                        time.sleep(0.5)
                        led.colorWipe(led.strip, Color(0,0,0))
                        counter = counter +1
                    counter = 0
                    state = "Drive"
                if state != "Drive":
                    scan("back")
                    if valid_path_found():
                        state = "Field of View Examination"

