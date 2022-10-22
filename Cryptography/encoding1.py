def convert_to_string(s):
    s = s.split(' ')
    s = [chr(int(i)) for i in s]
    s = ''.join(s)
    return s

print(convert_to_string('78 111 116 32 101 118 101 114 121 116 104 105 110 103 32 105 115 32 98 105 110 97 114 121 32 111 114 32 104 101 120'))