#author: Dan Ramos

import socket
import sys

# Create a TCP/IP socket
client = socket.socket()

# Connect the socket to the port where the server is listening
client.connect(('127.0.0.1', 50000))

#while True:
# print the response
recv_data = client.recv(4096)
print recv_data

#get input from user:
a = raw_input("Enter first integer number: ")
b = raw_input("Enter second integer number: ")

#send received data back
client.sendall(a)
client.sendall(b)
sum = client.recv(32)
print "\nResult from SuperAdder:\n"
print sum

# close the socket to clean up
client.close()

