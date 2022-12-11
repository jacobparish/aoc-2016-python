from aocd import data
import more_itertools as mit


def calc_checksum(seed_data: str, disk_size: int) -> str:
    disk_data = [c == "1" for c in seed_data]

    while len(disk_data) < disk_size:
        disk_data = disk_data + [False] + [not b for b in reversed(disk_data)]

    checksum = disk_data[:disk_size]

    while len(checksum) % 2 == 0:
        checksum = [b1 == b2 for b1, b2 in mit.chunked(checksum, 2)]

    return "".join("1" if b else "0" for b in checksum)


p1 = calc_checksum(data, 272)
p2 = calc_checksum(data, 35651584)
