# Python 3 server example
from http.server import HTTPServer, BaseHTTPRequestHandler
import constants

class TableServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("This is an example web server.", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((constants.IP_SERVER, constants.PORT), TableServer)
    print("Server started http://%s:%s" % (constants.IP_SERVER, constants.PORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")