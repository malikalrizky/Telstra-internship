# www.theforage.com - Telstra Cyber Task 3
# Firewall Server Handler

from http.server import BaseHTTPRequestHandler, HTTPServer

host = "localhost"
port = 8000

def block_request(self):
    self.send_error(403, "Request blocked due to firewall")

def handle_request(self):
    bad_headers = {
        "suffix": "%>//",
        "c1": "Runtime",
        "c2": "<%",
        "DNT": "1",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    if self.path == "/tomcatwar.jsp":
        for bad_header_key in bad_header_keys:
            for bad_header_key, bad_header_value in self.bad_headers.items():
                if bad_header_key in self.headers and self.headers[bad_header_key] == bad_header_value:
                    return block_request(self)

    self.send_response(200)
    self.send_header("content-type", "application/json")
    self.end_headers()

    self.wfile.write({ "success": True })


class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        handle_request(self)

    def do_POST(self):
        handle_request(self)

if __name__ == "__main__":        
    server = HTTPServer((host, port), ServerHandler)
    print("[+] Firewall Server")
    print("[+] HTTP Web Server running on: %s:%s" % (host, port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("[+] Server terminated. Exiting...")
    exit(0)