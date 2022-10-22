import base64
def base64_to_string(s):
    s = base64.b64decode(s)
    return s.decode('utf-8')

print(base64_to_string('RGF0YSBjYW4gYmUgcHJlc2VudGVkIGluIG1hbnkgd2F5cw=='))