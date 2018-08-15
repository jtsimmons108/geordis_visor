import socketserver, sys, os

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(str(self.data)[2:-1])
        self.show_image(str(self.data)[2:-1])

    def show_image(self, name):
        os.system('python /home/pi/python_files/geordis_visor/picture_viewer.py {}'.format(name))


if __name__ == "__main__":
    HOST, PORT = "", 9999

    # Create the server, binding on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
