from aocd import data
from parse import parse


def compute_decompressed_size(contents: str, recursive: bool = True) -> int:
    i = 0
    size = 0
    while i < len(contents):
        if contents[i] == "(":
            j = contents.index(")", i)
            amt, rpt = parse("{:d}x{:d}", contents[i + 1 : j])
            size += rpt * (
                compute_decompressed_size(contents[j + 1 : j + 1 + amt])
                if recursive
                else amt
            )
            i = j + 1 + amt
        else:
            size += 1
            i += 1
    return size


p1 = compute_decompressed_size(data, False)
p2 = compute_decompressed_size(data, True)
