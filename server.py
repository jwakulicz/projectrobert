from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import hello_car

robert = hello_car.Robert()
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
                <input type="submit" name="forward" value="forward" />
            </form>
            <form action="" method="post">
                <input type="submit" name="stop" value="stop" />
            </form>
            <form action="" method="post">
                <input type="submit" name="backward" value="backward" />
            </form>
            <form action="" method="post">
                <input type="submit" name="left" value="left" />
            </form>
            <form action="" method="post">
                <input type="submit" name="right" value="right" />
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
        
        if post_data == 'forward':
            robert.forward()
        elif post_data == 'stop':
            robert.stop()
        elif post_data == 'left':
            robert.left()
        elif post_data == 'right':
            robert_right()
        elif post_data == 'backward':
            robert_backward()
            
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
        robert.exit()
        http_server.server_close()