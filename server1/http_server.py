# Python 3 server example
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import constants

class TableServer(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        path = url.path
        query = parse_qs(url.query)
        
        if (path == '/'):
            if not bool(query):
                print(query)
                self.send_response(400)
                self.send_header("content-type", "text/plain")
                self.end_headers()
                self.wfile.write(bytes("No params detected.", "utf-8"))
            else:
                self.send_response(200)
                self.send_header("content-type", "text/plain")
                self.end_headers()
                self.wfile.write(bytes("This is an example web server.", "utf-8"))
        else:
            self.send_response(404)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("404 Error: Resource %s not found" % path, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((constants.IP_SERVER, constants.PORT), TableServer)
    print("Server started http://%s:%s" % (constants.IP_SERVER, constants.PORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")