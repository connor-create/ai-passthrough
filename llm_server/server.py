from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from urllib import parse

from models import Models, query_model

def _check_model(model_string: str):
    try:
        model = Models(model_string)
        return model
    except Exception as e:
        print(e)
        return None

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        model = parse.parse_qs(parse.urlparse(self.path).query).get('model', None)
        query_string = parse.parse_qs(parse.urlparse(self.path).query).get('query', None)
        if model is None:
            self._send_error("No model specified")
            return
        if query_string is None:
            self._send_error("No query or invalid query specified")
            return
        model = _check_model(model[0])
        if model is None:
            self._send_error("Invalid model specified")
            return 
        query_string = query_string[0]
        try:
            # Query model
            response_string = query_model(model, query_string)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(response_string, "utf-8"))
        except Exception as e:
            self._send_error(f"Unhandled/unspecific error: {str(e)}")

    def _send_error(self, error_string: str):
        self.send_response(400)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        error = str({
            "error": error_string
        })
        self.wfile.write(bytes(error, "utf-8"))
        return 

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