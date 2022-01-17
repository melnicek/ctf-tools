#!/usr/bin/env python3
import http.client

HOST = "127.0.0.1"
PORT = 0

conn = http.client.HTTPConnection(HOST, PORT)
conn.request("GET", "/")

res = conn.getresponse().read()
body = res.read()

print(body)
