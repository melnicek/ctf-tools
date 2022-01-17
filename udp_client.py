#!/usr/bin/env python3
import socket

RHOST = "127.0.0.1"
RPORT = 8990

client =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = b"8"
client.sendto(data, (RHOST, RPORT))
print("[sent to {0}:{1}]: {2}".format(RHOST, RPORT, data.decode("utf-8")))

data, addr = client.recvfrom(1024)
print("[recieved from {0}:{1}]: {2}".format(addr[0], addr[1], data.decode("utf-8")))