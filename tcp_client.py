#!/usr/bin/env python3
import socket

RHOST = "127.0.0.1"
RPORT = 8990

client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((RHOST, RPORT))

client.send(b"SYN")

response = client.recv(1024)
print(response)