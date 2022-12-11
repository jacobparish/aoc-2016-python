from aocd import data
from collections import defaultdict
import re
import hashlib
import bisect


def hash_n(bs: bytes, n: int = 0):
    h = hashlib.md5(bs)
    for _ in range(n):
        h = hashlib.md5(h.hexdigest().encode())
    return h


triple_re = re.compile("([0-9a-f])\\1\\1")
quintuple_re = re.compile("([0-9a-f])\\1\\1\\1\\1")


def find_keys(salt: str, nkeys: int, nstretches: int):
    i = 0
    pending_keys = defaultdict(list)
    keys = []

    while len(keys) < 64 or i < keys[63] + 1000:
        hexval = hash_n(f"{salt}{i}".encode(), nstretches).hexdigest()
        match = triple_re.search(hexval)
        if match is not None:
            for c in quintuple_re.findall(hexval):
                for j in pending_keys[c]:
                    if j > i - 1000:
                        bisect.insort(keys, j)
                pending_keys[c] = []
            pending_keys[match.group(1)].append(i)
        i += 1

    return keys[:nkeys]


p1 = find_keys(data, 64, 0)[-1]
p2 = find_keys(data, 64, 2016)[-1]
