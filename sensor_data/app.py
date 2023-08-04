from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from http.server import BaseHTTPRequestHandler, HTTPServer

color_sensor = ColorSensor("input_1")

def write_response(obj, text):
    text = str(text).encode("utf-8")
    obj.send_response(200)
    obj.send_header("Content-type", "text/plain")
    obj.end_headers()
    obj.wfile.write(text)

class RequestHandler(BaseHTTPRequestHandler):
    # On GET-Requests
    def do_GET(self):
        path = self.path
        if path == "/":
            write_response(self, "I AM ALIVE")
        elif path == "color"():
            color = color_sensor.color
            ambient = color_sensor.ambient_light_intensity
            reflection = color_sensor.reflected_light_intensity
            write_response(self, f"color: {color}\nambient light intensitiy: {ambient}\nreflected light intensity: {reflection}")
    # On POST-Requests
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        write_response(self, f"successfully received: '{post_data}'")

def run_server():
    httpd = HTTPServer(("", 80), RequestHandler)
    print("Server running on http://localhost:80")
    httpd.serve_forever()

run_server()