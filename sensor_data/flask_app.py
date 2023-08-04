from flask import Flask, render_template, jsonify, request
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor, UltrasonicSensor
from time import sleep

app = Flask(__name__)

# GLOBAL SENSORS
color_sensor = ColorSensor("input_1")
touch_sensor = TouchSensor("input_2")
# gyro_sensor = GyroSensor("input_3")
# ultrasonic_sensor = UltrasonicSensor("input_4")

@app.route("/")
def index():
    return render_template("index.html")

@app.rout("/get_data", methods=["GET"])
def get_data():
    return jsonify({
        "color" : color_sensor.color,
        "touch" : str(touch_sensor.is_pressed)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0")