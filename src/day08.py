from aocd import lines
from parse import parse
import numpy as np


screen = np.zeros((6, 50), dtype=bool)


for line in lines:
    [cmd, rest] = line.split(" ", 1)
    if cmd == "rect":
        w, h = parse("{:d}x{:d}", rest)
        screen[:h, :w] = True
    elif cmd == "rotate":
        _, xy, i, amt = parse("{} {}={:d} by {:d}", rest)
        if xy == "x":
            screen.T[i] = np.roll(screen.T[i], amt)
        elif xy == "y":
            screen[i] = np.roll(screen[i], amt)


p1 = np.sum(screen)

# print p2
for row in screen:
    print("".join("*" if p else " " for p in row))
