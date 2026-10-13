from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {"status": "healthy"}
        else:
            response = {
                "message": "Real-Time DevOps Project",
                "status": "Application Running",
                "version": os.getenv("APP_VERSION", "v1")
            }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

server = HTTPServer(("0.0.0.0", 8000), AppHandler)
print("Application running on port 8000", flush=True)
server.serve_forever()
