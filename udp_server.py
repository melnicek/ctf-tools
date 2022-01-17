#!/usr/bin/env python3
import socket, threading

BIND_HOST = "0.0.0.0"
BIND_PORT = 8990

server =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((BIND_HOST, BIND_PORT))

print("[+] Listening on port: {}".format(BIND_PORT))

while True:
    data, addr = server.recvfrom(1024)
    data = data.decode("utf-8")
    print("[recieved from {0}:{1}]: {2}".format(addr[0], addr[1], data))
    


    data = int(data) ** 2
    data = str(data).encode("utf-8")
    server.sendto(data, addr)
    print("[sent to {0}:{1}]: {2}".format(addr[0], addr[1], data.decode("utf-8")))
