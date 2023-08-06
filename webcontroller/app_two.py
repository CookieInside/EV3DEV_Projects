from flask import Flask, render_template, jsonify, request
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor, UltrasonicSensor, SoundSensor, InfraredSensor, LightSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
from ev3dev2.sound import Sound

sound = Sound()
app = Flask(__name__)

# GLOBAL MOTORS
motors = []

# GLOBAL SENSORS
sensors = []

def set_sync(type, motor, port):
    if type == "grosser EV3 Motor":
        motor = LargeMotor(port)
    elif type == "kleiner EV3 Motor":
        motor = MediumMotor(port)
    elif type == "grosser NXT Motor":
        motor = Motor(port)
    elif type == "nicht genutzt":
            motor = "not used"

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
    return render_template("testing.html")

@app.route("/get_sensor")
def get_sensor():
    color_values = ["keine Farbe erkennbar", "Schwarz", "Blau", "Gruen", "Gelb", "Rot", "Weiss", "Braun"]
    touch_values = ["wird nicht gedrueckt", "wird gedrueckt"]
    return jsonify({
        "color" : color_values[color_sensor.color],
        "touch" : touch_values[touch_sensor.is_pressed]
    })
# SPEAK
@app.route("/speak", methods=["POST"])
def speak():
    value = request.form["value"]
    sound.speak(value)
    return jsonify({"result" : "the robot said: '" + value + "'."})

# SYNC
@app.route("/sync", methods=["POST"])
def sync():
    # type-update
    A_type = request.form["A_type"]
    B_type = request.form["B_type"]
    C_type = request.form["C_type"]
    D_type = request.form["D_type"]
    one_type = request.form["one_type"]
    two_type = request.form["two_type"]
    three_type = request.form["three_type"]
    four_type = request.form["four_type"]
    # sync motor A
    set_sync(request.form["A_type"], motors[0], OUTPUT_A)
    set_sync(request.form["B_type"], motors[1], OUTPUT_B)
    set_sync(request.form["C_type"], motors[2], OUTPUT_C)
    set_sync(request.form["D_type"], motors[3], OUTPUT_D)

# SPEED UPDATER
@app.route("/speed_A", methods=["POST"])
def speed_A():
    return set_speed(motors[0], request.form["speed"])
    
@app.route("/speed_B", methods=["POST"])
def speed_B():
    return set_speed(motors[1], request.form["speed"])
    
@app.route("/speed_C", methods=["POST"])
def speed_C():
    return set_speed(motors[2], request.form["speed"])
    
@app.route("/speed_D", methods=["POST"])
def speed_D():
    return set_speed(motors[3], request.form["speed"])
    
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