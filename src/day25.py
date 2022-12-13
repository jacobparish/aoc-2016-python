from aocd import lines
from parse import parse

# The assembunny program puts two values into b and c, and then outputs the digits of
# a+b*c in binary forever (LSB first). So we parse b and c, and look for the first
# number n > b*c whose digits are alternating. I'm assuming the other inputs are the
# same, just with b and c varied.

(c,) = parse("cpy {:d} c", lines[1])
(b,) = parse("cpy {:d} b", lines[2])
n = 0
while n <= b * c:
    n = 4 * n + 2
p1 = n - b * c
