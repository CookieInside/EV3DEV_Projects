from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor, UltrasonicSensor, SoundSensor, InfraredSensor, LightSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import speech_recognition as sr

sensors = [None, None, None, None]

sensors[0] = sr.Microphone()

if type(sensors[0]) == sr.Microphone:
    print("y")
else:
    print("n")

#     /\      /\
#    /||\    /||\
#     ||      ||
#     ||      ||
#     \\      //
#      \\    //
#       \\  //
#        \\//
#         \/
#   Somehow working
#   ---------------
#   Use in app_two.py to recognize the kind of sensor and get the data properly in a for loop through the sensors list
#   In der Loop können die einzelnen Sensordaten dann in den durchgängen zum dict hinzugefügt werden z.Bsp.:
data = {}
data["sensor_one"] = "hier datenabfrage"