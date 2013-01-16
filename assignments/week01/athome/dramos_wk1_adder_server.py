#author: Dan Ramos

import socket
import sys

# Create a TCP/IP socket
ss = socket.socket()

# Bind the socket to the port
ss.bind(('127.0.0.1', 50000))

# Listen for incoming connections
ss.listen(1)

while True:
# Wait for a connection
 con, addr = ss.accept()

 con.sendall('\nFrom SuperAdder: Addition troubles, I will save the day! :)\n')

 a = con.recv(16)
 print a
 x = int(a)
 b = con.recv(16)
 print b
 y = int(b)

 z = x + y
 c = str(z)

 print c
 con.sendall(c)

#close connection
ss.close()

