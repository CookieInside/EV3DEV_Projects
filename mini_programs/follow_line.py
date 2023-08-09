from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank

tank = MoveTank(OUTPUT_B, OUTPUT_C)

DIST_PER_ROT = 10

def drive(distance, speed):
    tank.on_for_rotations(left_speed=speed, right_speed=speed, rotations=distance/DIST_PER_ROT)

def turn_right():
    tank.on_for_rotations(left_speed=100, right_speed=-100, rotations=0.25)

def turn_left():
    tank.on_for_rotations(left_speed=-100, right_speed=100, rotations=0.25)