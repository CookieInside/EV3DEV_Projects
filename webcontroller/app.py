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
    if A_type == "großer EV3 Motor":
        motor_A = LargeMotor(OUTPUT_A)
    elif A_type == "kleiner EV3 Motor":
        motor_A = MediumMotor(OUTPUT_A)
    elif A_type == "großer NXT Motor":
        motor_A = Motor(OUTPUT_A)
    elif A_type == "nicht genutzt":
        motor_A = "EMPTY"
    # sync motor B
    if B_type == "großer EV3 Motor":
        motor_B = LargeMotor(OUTPUT_B)
    elif B_type == "kleiner EV3 Motor":
        motor_B = MediumMotor(OUTPUT_B)
    elif B_type == "großer NXT Motor":
        motor_B = Motor(OUTPUT_B)
    elif B_type == "nicht genutzt":
        motor_B = "EMPTY"
    # sync motor C
    if C_type == "großer EV3 Motor":
        motor_C = LargeMotor(OUTPUT_C)
    elif C_type == "kleiner EV3 Motor":
        motor_C = MediumMotor(OUTPUT_C)
    elif C_type == "großer NXT Motor":
        motor_C = Motor(OUTPUT_C)
    elif C_type == "nicht genutzt":
        motor_C = "EMPTY"
    # sync motor D
    if D_type == "großer EV3 Motor":
        motor_D = LargeMotor(OUTPUT_D)
    elif D_type == "kleiner EV3 Motor":
        motor_D = MediumMotor(OUTPUT_D)
    elif D_type == "großer NXT Motor":
        motor_D = Motor(OUTPUT_D)
    elif D_type == "nicht genutzt":
        motor_D = "EMPTY"

# SPEED UPDATER
@app.route("/speed_A", methods=["POST"])
def speed_A():
    speed = int(request.form["speed"])
    if A_type == "großer NXT Motor":
        motor_A.speed_sp = speed
    else:
        motor_A.speed_sp = speed*10
    return jsonify({"result" : "speed was updated to " + str(speed)})

@app.route("/speed_B", methods=["POST"])
def speed_B():
    speed = int(request.form["speed"])
    if B_type == "großer NXT Motor":
        motor_B.speed_sp = speed
    else:
        motor_B.speed_sp = speed*10
    return jsonify({"result" : "speed was updated to " + str(speed)})

@app.route("/speed_C", methods=["POST"])
def speed_C():
    speed = int(request.form["speed"])
    if C_type == "großer NXT Motor":
        motor_C.speed_sp = speed
    else:
        motor_C.speed_sp = speed*10
    return jsonify({"result" : "speed was updated to " + str(speed)})

@app.route("/speed_D", methods=["POST"])
def speed_D():
    speed = int(request.form["speed"])
    if D_type == "großer NXT Motor":
        motor_D.speed_sp = speed
    else:
        motor_D.speed_sp = speed*10
    return jsonify({"result" : "speed was updated to " + str(speed)})


# POWER UPDATER
@app.route("/power_A", methods=["POST"])
def power_A():
    value = request.form["value"]
    if value == "on":
        motor_A.run_forever()
    else:
        motor_A.stop()
    return jsonify({"result" : "power was updated to " + str(value)})

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


if __name__ == "__main__":
    app.run(host="0.0.0.0")