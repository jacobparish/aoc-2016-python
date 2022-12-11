from aocd import data


# true = safe
row = [True, *(c == "." for c in data), True]
p1 = sum(row) - 2
p2 = p1

for n in range(1, 400000):
    next_row = [True] * len(row)
    for i in range(1, len(row) - 1):
        next_row[i] = row[i - 1] == row[i + 1]
    row = next_row
    num_safe = sum(row) - 2
    if n < 40:
        p1 += num_safe
    p2 += num_safe
