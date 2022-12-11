from aocd import lines
import more_itertools as mit
import numpy as np


def is_valid_triangle(lens):
    return (
        lens[0] < lens[1] + lens[2]
        and lens[1] < lens[0] + lens[2]
        and lens[2] < lens[0] + lens[1]
    )


p1 = 0
p2 = 0
for line_group in mit.chunked(lines, 3):
    arr = np.array([[int(l) for l in line.split()] for line in line_group])
    p1 += sum(is_valid_triangle(row) for row in arr)
    p2 += sum(is_valid_triangle(col) for col in arr.T)
