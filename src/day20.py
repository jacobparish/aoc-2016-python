from aocd import lines
import utils

ip_ranges = sorted(
    (ip_min, ip_max) for ip_min, ip_max in utils.parse_lines(lines, "{:d}-{:d}")
)

p1 = None
p2 = 0
min_unblocked = 0

for ip_min, ip_max in ip_ranges:
    if ip_min > min_unblocked:
        p2 += ip_min - min_unblocked
        if p1 is None:
            p1 = min_unblocked
    if ip_max > min_unblocked:
        min_unblocked = ip_max + 1
