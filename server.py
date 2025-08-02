import http.server
import socketserver
import os
import json
import socket

PORT = 8080
DIRECTORY = os.path.abspath(".")

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/list":
            video_dir = os.path.join(DIRECTORY, "localMovies")
            files = [f for f in os.listdir(video_dir) if f.lower().endswith(".mp4")]
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(files).encode())
        else:
            super().do_GET()

Handler.extensions_map.update({
    '.mp4': 'video/mp4',
})

os.chdir(DIRECTORY)

# Detectar IP local automáticamente
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # No se conecta realmente, solo fuerza la detección de la IP local
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "localhost"
    finally:
        s.close()
    return ip

local_ip = get_local_ip()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"📡 Servidor corriendo en:")
    print(f"   👉 Local:      http://localhost:{PORT}")
    print(f"   👉 En tu red:  http://{local_ip}:{PORT}")
    httpd.serve_forever()
