from http.server import BaseHTTPRequestHandler, HTTPServer
import time

from models import Models

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


class Server:
    def __init__(self) -> None:
        self.host_name = "localhost"
        self.server_port = 7080
        self.server = HTTPServer((self.host_name, self.server_port), Handler)

    def run(self) -> None:
        try:
            self.server.serve_forever()
        except Exception as e:
            print("Terminate server due to: ", e)

        self.server.server_close()
        print("Server stopped.")