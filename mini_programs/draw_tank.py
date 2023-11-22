from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, MoveTank

tank = MoveTank(OUTPUT_B, OUTPUT_C)

def drive(distance, speed):
    tank.on_for_rotations(left_speed=speed, right_speed=speed, rotations=distance)

def turn_right():
    tank.on_for_rotations(left_speed=100, right_speed=-100, rotations=0.25)

def turn_left():
    tank.on_for_rotations(left_speed=-100, right_speed=100, rotations=0.25)


base_distance = 5
for i in range(10):
    drive(distance=base_distance, speed=50)
    turn_right()
    drive(distance=base_distance, speed=50)
    turn_right()
    drive(distance=base_distance, speed=50)
    turn_right()
    base_distance += 3
    drive(distance=base_distance, speed=50)