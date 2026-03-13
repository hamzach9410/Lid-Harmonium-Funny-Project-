import http.server
import socketserver
import threading
import os

# Configuration
CHECKER_PORT = 3000
HARMONIUM_PORT = 3001
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CheckerHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Always serve index.html for the root or / check
        if path == "/" or path == "/index.html":
            return os.path.join(DIRECTORY, "index.html")
        return super().translate_path(path)

class HarmoniumHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Always serve harmonium.html for the root or / harmonium
        if path == "/" or path == "/harmonium.html":
            return os.path.join(DIRECTORY, "harmonium.html")
        return super().translate_path(path)

def serve_checker():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", CHECKER_PORT), CheckerHandler) as httpd:
        print(f"Angle Checker running at http://localhost:{CHECKER_PORT}")
        httpd.serve_forever()

def serve_harmonium():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", HARMONIUM_PORT), HarmoniumHandler) as httpd:
        print(f"i-Harmonium running at http://localhost:{HARMONIUM_PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    t1 = threading.Thread(target=serve_checker, daemon=True)
    t2 = threading.Thread(target=serve_harmonium, daemon=True)

    t1.start()
    t2.start()

    print("--- Web Servers Started ---")
    print(f"1. Angle Checker: http://localhost:{CHECKER_PORT}")
    print(f"2. i-Harmonium:  http://localhost:{HARMONIUM_PORT}")
    print("---------------------------")
    print("Press Ctrl+C to stop both servers.")

    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping servers...")
