from aocd import data
import hashlib


i = 1
chars1 = []
nchars2 = 0
chars2 = [None] * 8

while len(chars1) < 8 or nchars2 < 8:
    hexval = hashlib.md5(f"{data}{i}".encode()).hexdigest()
    if hexval[:5] == "00000":
        if len(chars1) < 8:
            chars1.append(hexval[5])
        try:
            pos = int(hexval[5])
            if chars2[pos] is None:
                chars2[pos] = hexval[6]
                nchars2 += 1
        except:
            pass
    i += 1


p1 = "".join(chars1)
p2 = "".join(chars2)
