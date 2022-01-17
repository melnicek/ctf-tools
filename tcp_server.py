#!/usr/bin/env python3
import socket, threading

BIND_HOST = "0.0.0.0"
BIND_PORT = 8990

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((BIND_HOST, BIND_PORT))

server.listen(5)

print("[+] Listening on port: {}".format(BIND_PORT))

def handle_client(clinet_socket):
    client_request = clinet_socket.recv(1024)
    
    print("[client_handler] Recived: {}".format(client_request))

    clinet_socket.send(b"ACK")

    clinet_socket.close()

while True:
    client, addr = server.accept()

    print("[main_loop] Connection from {0}:{1}".format(addr[0], addr[1]))

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

