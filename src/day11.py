from aocd import data, lines, numbers
from parse import findall
import itertools as it
import more_itertools as mit
import numpy as np
import collections as col
import heapq
import string
import utils


p1 = None
p2 = None

floors = []

for line in lines:
    floor = []
    for (rtg,) in findall("{:l} generator", line):
        floor.append((rtg, "rtg"))
    for (mc,) in findall("{:l}-compatible microchip", line):
        floor.append((mc, "mc"))
    floors.append(floor)
    print(floor)


target = []

# dijkstra maybe idk

#
#
#
#


print("p1:", p1)
print("p2:", p2)

raise
