from flask import Flask, render_template, jsonify, request
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, Motor
from ev3dev2.sound import Sound


sound = Sound()
app = Flask(__name__)

# GLOBAL MOTORS
A_type = ""
B_type = ""
C_type = ""
D_type = ""
motor_A = Motor(OUTPUT_A)
motor_B = Motor(OUTPUT_B)
motor_C = Motor(OUTPUT_C)
motor_D = Motor(OUTPUT_D)

# GLOBAL SENSORS
one_type = ""
two_type = ""
three_type = ""
four_type = ""


@app.route("/")
def index():
    return render_template("index.html")

# SPEAK
@app.route("/speak", methods=["POST"])
def speak():
    value = request.form["value"]
    sound.speak(value)
    return jsonify({"result" : "the robot said: '" + value + "'."})

# SYNC
@app.rout("/sync", methods=["POST"])
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
    set_sync(request.form["A_type"], motor_A, OUTPUT_A)
    set_sync(request.form["B_type"], motor_B, OUTPUT_B)
    set_sync(request.form["C_type"], motor_C, OUTPUT_C)
    set_sync(request.form["D_type"], motor_D, OUTPUT_D)

# SPEED UPDATER
@app.route("/speed_A", methods=["POST"])
def speed_A():
    set_speed(motor_A, request.form["speed"])

@app.route("/speed_B", methods=["POST"])
def speed_B():
    set_speed(motor_B, request.form["speed"])

@app.route("/speed_C", methods=["POST"])
def speed_C():
    set_speed(motor_C, request.form["speed"])

@app.route("/speed_D", methods=["POST"])
def speed_D():
    set_speed(motor_D, request.form["speed"])

# POWER UPDATER
@app.route("/power_A", methods=["POST"])
def power_A():
    set_speed(motor_A, request.form["value"])

@app.route("/power_B", methods=["POST"])
def power_B():
    value = request.form["value"]
    if value == "on":
        motor_B.run_forever()
    else:
        motor_B.stop()
    return jsonify({"result" : "power was updated to " + str(value)})

@app.route("/power_C", methods=["POST"])
def power_C():
    value = request.form["value"]
    if value == "on":
        motor_C.run_forever()
    else:
        motor_C.stop()
    return jsonify({"result" : "power was updated to " + str(value)})

@app.route("/power_D", methods=["POST"])
def power_D():
    value = request.form["value"]
    if value == "on":
        motor_D.run_forever()
    else:
        motor_D.stop()
    return jsonify({"result" : "power was updated to " + str(value)})


def set_sync(type, motor, port):
    match type:
        case "großer EV3 Motor":
            motor = LargeMotor(port)
        case "kleiner EV3 Motor":
            motor = MediumMotor(port)
        case "großer NXT Motor":
            motor = Motor(port)
        case "nicht genutzt":
            motor = "not used"

def set_speed(motor, speed):
    if A_type == "großer NXT Motor":
        motor.speed_sp = speed
    else:
        motor.speed_sp = speed*10
    return jsonify({"result" : "power was updated to " + str(speed)})

if __name__ == "__main__":
    app.run(host="0.0.0.0")