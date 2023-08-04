from flask import Flask, render_template, jsonify, request
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor, UltrasonicSensor
from time import sleep
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4


app = Flask(__name__)

# GLOBAL SENSORS
color_sensor = ColorSensor(INPUT_1)
touch_sensor = TouchSensor(INPUT_2)
# gyro_sensor = GyroSensor("input_3")
# ultrasonic_sensor = UltrasonicSensor("input_4")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_data", methods=["GET"])
def get_data():
    color_values = ["keine Farbe erkennbar", "Schwarz", "Blau", "Gruen", "Gelb", "Rot", "Weiss", "Braun"]
    touch_values = ["wird nicht gedrueckt", "wird gedrueckt"]
    return jsonify({
        "color" : color_values[color_sensor.color],
        "touch" : touch_values[touch_sensor.is_pressed]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    print("Flask server stopped")