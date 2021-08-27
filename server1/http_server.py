# Python 3 server example
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import constants

class TableServer(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        path = url.path
        query = parse_qs(url.query)

        for k in query.keys(): # Query string values can be lists. We get the first value only
            query[k] = query[k][0]
        
        if (path == '/'):
            if len(query) < 3 or not ('initValue' in query and 'ir' in query and 'months' in query):
                self.send_response(400)
                self.send_header("content-type", "text/plain")
                self.end_headers()
                self.wfile.write(bytes("Missing arguments on query string (initValue, ir, months)", "utf-8"))
            elif verify_arguments(query['initValue'], query['ir'], query['months']) < 0:
                self.send_response(400)
                self.send_header("content-type", "text/plain")
                self.end_headers()
                self.wfile.write(bytes("Incorrect values: some query params has 'str' instead of 'float'", "utf-8"))
            else:
                initValue = float(query['initValue'])
                ir = float(query['ir'])
                months = float(query['months'])
                res = generate_table(initValue, ir, months)
                
                self.send_response(200)
                self.send_header("content-type", "text/plain")
                self.end_headers()
                self.wfile.write(bytes(res, "utf-8"))
        
        elif (path == '/ping'):
            self.send_response(200)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Connection established", "utf-8"))
        
        elif (path == '/help'):
            self.send_response(200)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Welcome to Generate Repayment Table Server!\nAvailable resources: /, /help, /ping\n\n", "utf-8"))
            self.wfile.write(bytes("RESOURCES\n", "utf-8"))
            self.wfile.write(bytes("/ (usage: /?initValue=FLOAT&ir=FLOAT&months=INT\n", "utf-8"))
            self.wfile.write(bytes("    This resource returns a repayment table according to initial capital, interest rate and total months to pay.\n\n", "utf-8"))
            self.wfile.write(bytes("/help (usage: /help\n", "utf-8"))
            self.wfile.write(bytes("    This resource explains all available server interactions and resources.\n\n", "utf-8"))
            self.wfile.write(bytes("/ping (usage: /ping\n", "utf-8"))
            self.wfile.write(bytes("    This resource helps to test if server connection was established.\n\n", "utf-8"))

        else:
            self.send_response(404)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("404 Error: Resource %s not found" % path, "utf-8"))

def verify_arguments(val, ir, m):
    try:
        float(val)
        float(ir)
        float(m)
    except ValueError:
        return -1
    return 0

def generate_table(value, ir, total_months):
    desc = f'''************************
* Initial capital : {value}
* Interest rate   : {ir} %
* Total periods   : {total_months}
************************\n\n'''

    value = float(value)
    ir = float(ir)/100
    total_months = int(total_months)

    exp_interest = (1+ir)**total_months
    monthly_payment = (value * ir * exp_interest)/(exp_interest - 1)
    
    # Header
    table_string =  f'|{"":->5}+{"":->17}+{"":->17}+{"":->17}+{"":->19}|\n'
    table_string += f'|{"Month":>5}|{"Monthly payment":>17}|{"Debt payment":>17}|{"Interest payment":>17}|{"Remaining debt":>19}|\n'
    table_string += f'|{"":->5}+{"":->17}+{"":->17}+{"":->17}+{"":->19}|\n'
    
    # First row
    table_string += f'|{"0":>5}|{"":>17}|{"":>17}|{"":>17}|{value:>17,.2f} $|\n'

    prev_value = value
    # Generate each row
    for i in range(1, total_months+1):
        ir_payment = prev_value*ir
        cap_payment = monthly_payment - ir_payment
        amount = prev_value - cap_payment
        table_string += f'|{i:>5}|{monthly_payment:>15,.2f} $|{cap_payment:>15,.2f} $|{ir_payment:>15,.2f} $|{amount:>17,.2f} $|\n'
        prev_value = amount
    table_string += f'|{"":->5}+{"":->17}+{"":->17}+{"":->17}+{"":->19}|\n'

    return desc + table_string + '\n'

if __name__ == "__main__":
    webServer = HTTPServer((constants.IP_SERVER, constants.PORT), TableServer)
    print("Server started http://%s:%s" % (constants.IP_SERVER, constants.PORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")