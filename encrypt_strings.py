import sys, os
from itertools import cycle

XOR_FUNCTION='''void XOR(char * data, size_t data_len, char * key, size_t key_len) {
	int j = 0;
	for (int i = 0; i < data_len; i++) {
		if (j == key_len - 1) j = 0;

		data[i] = data[i] ^ key[j];
		j++;
	}
}
'''

def XOR(string, key):
    # return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(string, cycle(key)))
    j = 0
    result = []
    for i in range(len(string)):
        result.append(string[i] ^ key[j]) 
        j += 1
        if j >= len(key):
            j = 0
    return result


def Hexify(arr):
    result = ""
    for num in arr:
        if len(hex(num)) == 3:
            result += hex(num).replace("0x", "\\x0")
        else:
            result += hex(num).replace("0x", "\\x")
    return result


def UseString(string: str):
    var_name = string.lower()
    key = os.urandom(4)
    enc = XOR(bytes(string, encoding='ascii'), key)
    print()
    print('unsigned char {}[] = \"{}\";'.format(var_name, Hexify(enc)))
    print('int {}_len = {};'.format(var_name, len(string)))
    print('unsigned char {}_key[] = \"{}\";'.format(var_name, Hexify(key)))
    print('int {}_key_len = {};'.format(var_name, len(key)))
    print("XOR({0}, {0}_len, {0}_key, {0}_key_len);".format(var_name))
    


def main():
    if len(sys.argv) != 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit()
    print(XOR_FUNCTION)
    with open(sys.argv[1], "r") as f:
        for line in f:
            line = line.strip()
            UseString(line)


if __name__ == "__main__":
    main()
