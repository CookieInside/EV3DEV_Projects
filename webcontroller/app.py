from flask import Flask, render_template, jsonify, request
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, Motor
from ev3dev2.sound import Sound


sound = Sound()

motor_A = LargeMotor(OUTPUT_A)
motor_B = LargeMotor(OUTPUT_B)
motor_C = Motor(OUTPUT_C)
motor_D = MediumMotor(OUTPUT_D)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# SPEAK
@app.route("/speak", methods=["POST"])
def speak():
    value = request.form["value"]
    sound.speak(value)
    return jsonify({"result" : "the robot said: '" + value + "'."})


# SPEED UPDATER
@app.route("/speed_A", methods=["POST"])
def speed_A():
    value = int(request.form["value"])
    #motor_A.run_forever()
    motor_A.speed_sp = value*10
    return jsonify({"result" : "speed was updated to " + str(value)})

@app.route("/speed_B", methods=["POST"])
def speed_B():
    value = int(request.form["value"])
    #motor_B.run_forever()
    motor_B.speed_sp = value*10
    return jsonify({"result" : "speed was updated to " + str(value)})

@app.route("/speed_C", methods=["POST"])
def speed_C():
    value = int(request.form["value"])
    #motor_C.run_forever()
    motor_C.on(value)
    return jsonify({"result" : "speed was updated to " + str(value)})

@app.route("/speed_D", methods=["POST"])
def speed_D():
    value = int(request.form["value"])
    #motor_D.run_forever()
    motor_D.speed_sp = value*10
    return jsonify({"result" : "speed was updated to " + str(value)})


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