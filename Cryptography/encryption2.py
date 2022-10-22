# substitution ciphers decryption
# this need to be solved manually by the user
dict = {"e": "a",
        "r": "s",
        "k": "g",
        "a": "e",
        "x": "u",
        "w": "c",
        "y": "t",
        "g": "m",
        "s": "r",
        "t": "y",
        "u": "s",
        "z": "b",
        "m": "k",
        "q": "p"
        }


def decrypt(cipher):
    plain = ""
    for c in cipher:
        if c in dict:
            plain += dict[c]
        else:
            plain += c
    return plain


print(decrypt(
    'rxzryiyxyion wiqhasr wen za zsoman feislt aerilt, er lonk er yha wiqhas yauy ir lonk anoxkh, end wonyeinr anoxkh woggonlt xrad whesewyasr.'))
