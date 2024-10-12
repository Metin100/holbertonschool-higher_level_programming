#!/usr/bin/python3
import http.server
import json


class BasicServer(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')  # Hata mesajı için içerik türü
            self.end_headers()
            error_response = {"error": "404 Not Found", "message": "FAIL - Undefined endpoint"}  # JSON formatında hata yanıtı
            self.wfile.write(json.dumps(error_response).encode('utf-8'))  # Hata yanıtını JSON olarak gönderiyoruz


server = ('', 8000)
httpd = http.server.HTTPServer(server, BasicServer)
print('Server is running on port 8000...')
httpd.serve_forever()
