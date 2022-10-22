# rol13 decoder`
def rol13(s):
    return s.translate(str.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"))


print(rol13('Vgf abg npghnyyl gung uneq'))
