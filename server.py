from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import hello_car

host_port = 8000

class MyServer(BaseHTTPRequestHandler):
    """ A special implementation of BaseHTTPRequestHander for reading data from
        and control GPIO of a Raspberry Pi
    """

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        html = '''
            <html>
            <body style="width:960px; margin: 20px auto;">
            <h1>Welcome to ROBERT</h1>
            <form action="" method="post">
                <input type="submit" name="start" value="start" />
            </form>
            <form action="" method="post">
                <input type="submit" name="stop" value="stop" />
            </form>
            </body>
            </html>
        '''
        self.do_HEAD()
        self.wfile.write(html.format().encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])    # Get the size of data
        post_data = self.rfile.read(content_length).decode("utf-8")   # Get the data
        post_data = post_data.split("=")[1]    # Only keep the value
        print(post_data)

        if post_data == 'start':
            robert = hello_car.Robert()
        elif post_data == 'stop':
            robert.exit()
            
        self._redirect('/')    # Redirect back to the root url

if __name__ == '__main__':
    print("Enter raspberry pi ip address")
    host_name = raw_input()

    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        print("Server Stopped")
        # hello_car.exit()
        http_server.server_close()