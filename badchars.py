#!/usr/bin/env python3

def generate_string():
    bc = ""
    for x in range(1, 256):
        bc += "\\x{:02x}".format(x)
    return bc

def generate_bytes():
    return str.encode(generate_string())

def generate_print():
    print(generate_string())

if __name__ == "__main__":
    generate_print()