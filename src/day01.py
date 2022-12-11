from aocd import data
import numpy as np
import utils


pos = np.array((0, 0), dtype=int)
dir = np.array((1, 0), dtype=int)
rotations = {
    "R": np.array(((0, -1), (1, 0)), dtype=int),
    "L": np.array(((0, 1), (-1, 0)), dtype=int),
}
visited = set(tuple(pos))
p2 = None
for d, amt in utils.parse_lines(data.split(", "), "{}{:d}"):
    dir = np.matmul(rotations[d], dir)
    for _ in range(amt):
        pos += dir
        if tuple(pos) in visited and p2 is None:
            p2 = sum(abs(x) for x in pos)
        visited.add(tuple(pos))

p1 = sum(abs(x) for x in pos)
