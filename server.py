import RPi.GPIO as GPIO
import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import hello_car


host_name = '192.168.15.9'    # ip address of Pi
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
            <h1>Welcome to my Raspberry Pi</h1>
            <p>Current GPU temperature is {}</p>
            <form action="" method="post">
                <input type="submit" name="start" value="start" />
            </form>
            <form action="" method="post">
                <input type="submit" name="stop" value="stop" />
            </form>
            </body>
            </html>
        '''
        temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
        self.do_HEAD()
        self.wfile.write(html.format(temp[5:]).encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])    # Get the size of data
        post_data = self.rfile.read(content_length).decode("utf-8")   # Get the data
        post_data = post_data.split("=")[1]    # Only keep the value
        print(post_data)

        if post_data == 'start':
            print("start button was clicked")
        elif post_data == 'stop':
            print("stop button was clicked")

        # GPIO setup here

        # # Example of a POST request here
        # if post_data == 'Go':
        #     #GPIO.output(18, GPIO.HIGH) make it go
        # else:
        #     #GPIO.output(18, GPIO.LOW) stop

        self._redirect('/')    # Redirect back to the root url

if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        print("Server Stopped")
        # hello_car.exit()
        http_server.server_close()