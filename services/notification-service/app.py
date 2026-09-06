#!/usr/bin/env python3
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/health", "/api/notifications/health"):
            self.respond(200, {
                "status": "UP",
                "service": os.getenv("SERVICE_NAME", "modern-notification-service"),
                "stack": "modern",
            })
            return

        self.respond(404, {"error": "not_found", "path": self.path})

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args), flush=True)

    def respond(self, status, body):
        data = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main():
    port = int(os.getenv("PORT", "8080"))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"modern-notification-service listening on {port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
