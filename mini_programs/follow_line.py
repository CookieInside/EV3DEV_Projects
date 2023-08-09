from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank

DIST_PER_ROT = 10

color_sensor = ColorSensor(INPUT_1)
tank = MoveTank(OUTPUT_B, OUTPUT_C)

def drive(distance, speed):
    tank.on_for_rotations(left_speed=speed, right_speed=speed, rotations=distance/DIST_PER_ROT)

def turn_right():
    tank.on_for_rotations(left_speed=100, right_speed=-100, rotations=0.25)

def turn_left():
    tank.on_for_rotations(left_speed=-100, right_speed=100, rotations=0.25)

def turn(degrees):
    tank.on_for_rotations(left_speed=-100, right_speed=100, rotations=degrees/360)

def find_line():
    iterator = 1
    while color_sensor.color != 1:
        turn(iterator)
        iterator += 1
        iterator *= -1

while True:
    while color_sensor.color == 1:
        drive(1)
    find_line()