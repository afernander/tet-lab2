# Python 3 server example
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import constants

class TableServer(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(self.path)
        
        if not bool(query):
            print(query)
            self.send_response(400)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("No params detected.", "utf-8"))
        else:
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