from aocd import lines
from collections import Counter


counters = [Counter(line[i] for line in lines) for i in range(len(lines[0]))]
p1 = "".join(counter.most_common()[0][0] for counter in counters)
p2 = "".join(counter.most_common()[-1][0] for counter in counters)
