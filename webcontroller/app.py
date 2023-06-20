from flask import Flask, render_template, jsonify, request
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
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

def set_sync(type, motor, port):
    match type:
        case "grosser EV3 Motor":
            motor = LargeMotor(port)
        case "kleiner EV3 Motor":
            motor = MediumMotor(port)
        case "grosser NXT Motor":
            motor = Motor(port)
        case "nicht genutzt":
            motor = "not used"

def set_speed(type, motor, speed):
    if type == "grosser NXT Motor":
        motor.speed_sp = int(speed)
    else:
        motor.speed_sp = int(speed)*10
    return jsonify({"result" : f"power was updated to {speed}"})

def set_power(motor, value):
    if value == "on":
        motor.run_forever()
    else:
        motor.stop()
        return jsonify({"result" : f"the motor is now {value}"})

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
    return set_speed(A_type, motor_A, request.form["speed"])
    
@app.route("/speed_B", methods=["POST"])
def speed_B():
    return set_speed(B_type, motor_B, request.form["speed"])
    
@app.route("/speed_C", methods=["POST"])
def speed_C():
    return set_speed(C_type, motor_C, request.form["speed"])
    
@app.route("/speed_D", methods=["POST"])
def speed_D():
    return set_speed(D_type, motor_D, request.form["speed"])
    
# POWER UPDATER
@app.route("/power_A", methods=["POST"])
def power_A():
    return set_power(motor_A, request.form["value"])

@app.route("/power_B", methods=["POST"])
def power_B():
    return set_power(motor_B, request.form["value"])

@app.route("/power_C", methods=["POST"])
def power_C():
    return set_power(motor_C, request.form["value"])

@app.route("/power_D", methods=["POST"])
def power_D():
    return set_power(motor_D, request.form["value"])


if __name__ == "__main__":
    app.run(host="0.0.0.0")