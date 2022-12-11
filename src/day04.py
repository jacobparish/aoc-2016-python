from aocd import lines
from parse import parse
from collections import Counter
import string


p1 = 0
p2 = None

for line in lines:
    name, id, cs = parse("{}-{:d}[{}]", line)
    letters = Counter(c for c in name if c != "-")
    if cs == "".join(
        k[0] for k in sorted(letters.items(), key=lambda k: (-k[1], k[0]))[:5]
    ):
        p1 += id

        decoded_name = ""
        for c in name:
            if c == "-":
                decoded_name += " "
            else:
                i = (string.ascii_lowercase.index(c) + id) % 26
                decoded_name += string.ascii_lowercase[i]
        if decoded_name == "northpole object storage":
            p2 = id
