import socket
import sys

HOST, PORT = "192.168.1.48", 9999
filename = 'resize'
data = bytes(filename, 'utf-8')

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(data)

finally:
    sock.close()

#print("Sent:     {}".format(data))
