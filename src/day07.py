from aocd import lines
import more_itertools as mit

p1 = 0
p2 = 0

for line in lines:
    abbas = [False, False]
    abas = set()
    babs = set()

    for i, part in enumerate(mit.split_at(line, lambda c: c in "[]")):
        for x, y, z, w in mit.sliding_window(part, 4):
            if x == w and y == z and x != y:
                abbas[i % 2] = True
        for x, y, z in mit.sliding_window(part, 3):
            if x == z and x != y:
                if i % 2 == 0:
                    abas.add((x, y))
                else:
                    babs.add((y, x))

    p1 += abbas[0] and not abbas[1]
    p2 += not abas.isdisjoint(babs)
