from flask import Flask, render_template, jsonify, request
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent
from ev3dev2.sound import Sound
import socket


port = 8080

# Socket erstellen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Socket an die lokale IP-Adresse und den Port binden
server_socket.bind(('0.0.0.0', port))

# Socket in den Listening-Modus versetzen
server_socket.listen(1)

print('Server lauscht auf Port', port)

# Auf eingehende Verbindungen warten
while True:
    # Verbindung akzeptieren
    client_socket, client_address = server_socket.accept()
    
    print('Neue Verbindung von:', client_address)
    
    # Daten von Client empfangen
    data = client_socket.recv(1024)
    
    # Empfangene Daten verarbeiten
    # ...
    
    # Verbindung schließen
    client_socket.close()



sound = Sound()

motor_A = LargeMotor(OUTPUT_A)
motor_B = LargeMotor(OUTPUT_B)
motor_C = LargeMotor(OUTPUT_C)
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
    motor_A.speed_sp(value)
    return jsonify({"result" : "speed was updated to " + value})

@app.route("/speed_B", methods=["POST"])
def speed_B():
    value = int(request.form["value"])
    motor_B.speed_sp(value)
    return jsonify({"result" : "speed was updated to " + value})

@app.route("/speed_C", methods=["POST"])
def speed_C():
    value = int(request.form["value"])
    motor_C.speed_sp(value)
    return jsonify({"result" : "speed was updated to " + value})

@app.route("/speed_D", methods=["POST"])
def speed_D():
    value = int(request.form["value"])
    motor_D.speed_sp(value)
    return jsonify({"result" : "speed was updated to " + value})


# POWER UPDATER
@app.route("/power_A", methods=["POST"])
def power_A():
    value = bool(request.form["value"])
    if value:
        motor_A.run_forever()
    else:
        motor_A.stop()
    return jsonify({"result" : "power was updated to " + value})

@app.route("/power_B", methods=["POST"])
def power_B():
    value = bool(request.form["value"])
    if value:
        motor_B.run_forever()
    else:
        motor_B.stop()
    return jsonify({"result" : "power was updated to " + value})

@app.route("/power_C", methods=["POST"])
def power_C():
    value = bool(request.form["value"])
    if value:
        motor_C.run_forever()
    else:
        motor_C.stop()
    return jsonify({"result" : "power was updated to " + value})

@app.route("/power_D", methods=["POST"])
def power_D():
    value = bool(request.form["value"])
    if value:
        motor_D.run_forever()
    else:
        motor_D.stop()
    return jsonify({"result" : "power was updated to " + value})



if __name__ == "__main__":
    app.run()