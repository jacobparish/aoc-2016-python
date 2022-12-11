from aocd import lines
from parse import parse
from sympy.ntheory.modular import crt


moduli = []
residues = []

for line in lines:
    n, size, start = parse(
        "Disc #{:d} has {:d} positions; at time=0, it is at position {:d}.", line
    )
    moduli.append(size)
    residues.append(-start - n)

p1 = crt(moduli, residues)[0]

residues.append(-len(lines) - 1)
moduli.append(11)

p2 = crt(moduli, residues)[0]
