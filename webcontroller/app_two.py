from flask import Flask, render_template, jsonify, request
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor, UltrasonicSensor, SoundSensor, InfraredSensor, LightSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.motor import LargeMotor, MediumMotor, Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sound import Sound


# GLOBAL VARS
sound = Sound()
app = Flask(__name__)


# GLOBAL MOTORS
motors = [None, None, None, None]

# GLOBAL SENSORS
sensors = [None, None, None, None]


def get_sensor_value(sensor):
    COLOR_VALUES = ["keine Farbe erkennbar", "Schwarz", "Blau", "Gruen", "Gelb", "Rot", "Weiss", "Braun"]
    TOUCH_VALUES = ["Tastsensor wird nicht gedrückt", "Tastsensor wird gedrückt"]
    if type(sensor) == TouchSensor:
        return TOUCH_VALUES[sensor.is_pressed]
    if type(sensor) == ColorSensor:
        return "Farbe: " + COLOR_VALUES[sensor.color] + "<br>Umgebungslichtintensität: " + str(sensor.ambient_light_intensity) + "<br> Reflektierte Lichtintensität: " + str(sensor.reflected_light_intensity)
    if sensor == "not used":
        return "Sensor wird nicht genutzt"

def post_sensor():
    data = {}
    data["port_1"] = get_sensor_value(sensors[0])
    data["port_2"] = get_sensor_value(sensors[1])
    data["port_3"] = get_sensor_value(sensors[2])
    data["port_4"] = get_sensor_value(sensors[3])
    return data

def set_sync(type, device_type, device_index, port):
    if device_type == "motor":
        if type == "grosser EV3 Motor":
            motors[device_index] = LargeMotor(port)
        elif type == "kleiner EV3 Motor":
            motors[device_index] = MediumMotor(port)
        elif type == "grosser NXT Motor":
            motors[device_index] = Motor(port)
        elif type == "nicht genutzt":
            motors[device_index] = "not used"
    elif device_type == "sensor":
        if type == "Tastsensor":
            sensors[device_index] = TouchSensor(port)
        elif type == "Farbsensor":
            sensors[device_index] = ColorSensor(port)
        elif type == "nicht genutzt":
            sensors[device_index] = "not used"

def set_speed(motor, speed):
    motor.on(speed=speed)
    return jsonify({"result" : "speed was updated to " + speed + "%"})

def set_power(motor, value):
    if value == "on":
        motor.run_forever()
    else:
        motor.off()
        return jsonify({"result" : "the motor is now " + value})

@app.route("/")
def index():
    return render_template("testing_sensor_extension.html")

@app.route("/get_sensor")
def get_sensor():
    return jsonify(post_sensor())
# SPEAK
@app.route("/speak", methods=["POST"])
def speak():
    value = request.form["value"]
    sound.speak(value)
    return jsonify({"result" : "the robot said: '" + value + "'."})

# SYNC
@app.route("/sync", methods=["POST"])
def sync():
    data = request.get_json()
    print("||||||||||||||||||||||||||||||||||" + str(data) + "||||||||||||||||||||||||||||||||||")
    set_sync(data["a_type"], "motor", 0, OUTPUT_A)
    set_sync(data["b_type"], "motor", 1, OUTPUT_B)
    set_sync(data["c_type"], "motor", 2, OUTPUT_C)
    set_sync(data["d_type"], "motor", 3, OUTPUT_D)
    set_sync(data["one_type"], "sensor", 0, INPUT_1)
    set_sync(data["two_type"], "sensor", 1, INPUT_2)
    set_sync(data["three_type"], "sensor", 2, INPUT_3)
    set_sync(data["four_type"], "sensor", 3, INPUT_4)
    return jsonify({"result" : "sync method called"})
# SPEED UPDATER
@app.route("/speed_A", methods=["POST"])
def speed_A():
    return set_speed(motors[0], int(request.form["speed"]))
    
@app.route("/speed_B", methods=["POST"])
def speed_B():
    return set_speed(motors[1], int(request.form["speed"]))
    
@app.route("/speed_C", methods=["POST"])
def speed_C():
    return set_speed(motors[2], int(request.form["speed"]))
    
@app.route("/speed_D", methods=["POST"])
def speed_D():
    return set_speed(motors[3], int(request.form["speed"]))
    
# POWER UPDATER
@app.route("/power_A", methods=["POST"])
def power_A():
    return set_power(motors[0], request.form["value"])

@app.route("/power_B", methods=["POST"])
def power_B():
    return set_power(motors[0], request.form["value"])

@app.route("/power_C", methods=["POST"])
def power_C():
    return set_power(motors[0], request.form["value"])

@app.route("/power_D", methods=["POST"])
def power_D():
    return set_power(motors[0], request.form["value"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)