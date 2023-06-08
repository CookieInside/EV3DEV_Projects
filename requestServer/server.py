from ev3dev2.sound import Sound
from http.server import BaseHTTPRequestHandler, HTTPServer

sound = Sound()

class RequestHandler(BaseHTTPRequestHandler):
    # On GET-Requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'some value')
    # On POST-Requests
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        sound.speak(post_data)
        response = "success"
        self.send_response(200)
        self.send_header('Content-type', 'text/html') 
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

def run_server():
    httpd = HTTPServer(("", 8000), RequestHandler)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()

run_server()