def hex_to_string(s):
    s = s.split(' ')
    s = [chr(int(i, 16)) for i in s]
    s = ''.join(s)
    return s

print(hex_to_string('48 65 78 20 65 6e 63 6f 64 69 6e 67 20 69 73 20 76 65 72 79 20 63 6f 6d 6d 6f 6e 20 69 6e 20 63 72 79 70 74 6f'))