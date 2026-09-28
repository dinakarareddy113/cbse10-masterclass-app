import http.server
import socketserver
import os
import mimetypes

class RobustAPKHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS and caching headers for mobile browsers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def guess_type(self, path):
        if path.endswith('.apk'):
            return 'application/vnd.android.package-archive'
        return super().guess_type(path)

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

if __name__ == '__main__':
    web_dir = os.path.join(os.path.dirname(__file__), '..', 'mobile_test')
    os.chdir(web_dir)
    mimetypes.add_type('application/vnd.android.package-archive', '.apk')
    
    port = 8080
    server = ThreadedHTTPServer(('0.0.0.0', port), RobustAPKHandler)
    print(f"Serving {web_dir} on 0.0.0.0:{port} with APK MIME support...", flush=True)
    server.serve_forever()
