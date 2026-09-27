import http.server
import socketserver
import socket
import os
import sys

DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "mobile_test"))
PORT = 8080

class DualStackServer(socketserver.ThreadingTCPServer):
    address_family = socket.AF_INET6
    allow_reuse_address = True
    daemon_threads = True

    def server_bind(self):
        try:
            self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        except Exception as e:
            print("Note: Could not set IPV6_V6ONLY:", e)
        super().server_bind()

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {self.address_string()} - {format % args}\n")

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    print(f"Dual-stack HTTP server starting on port {PORT} for directory:\n  {DIRECTORY}")
    server = DualStackServer(("", PORT), Handler)
    print(f"Ready! Serving on:")
    print(f"  - http://localhost:{PORT}")
    print(f"  - http://127.0.0.1:{PORT}")
    print(f"  - http://[::1]:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")
