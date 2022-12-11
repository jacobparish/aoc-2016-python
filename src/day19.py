from aocd import data


def find_last_by_eliminating_next(n: int) -> int:
    n_ = n
    blen = 0
    while n_ >= 2:
        blen += 1
        n_ //= 2
    return 2 * (n % 2**blen) + 1


def find_last_by_elmininating_opposite(n: int) -> int:
    if n == 1:
        return 1
    # I have no idea why this works, but this seems to be the pattern. It depends
    # somehow on the first digit of the ternary representation of n.
    mst = n - 1
    tlen = 0
    while mst >= 3:
        mst //= 3
        tlen += 1
    if mst == 1:
        return (n - 1) % (3**tlen) + 1
    else:
        return 3**tlen + 2 * ((n - 1) % 3**tlen + 1)


nelves = int(data)
p1 = find_last_by_eliminating_next(nelves)
p2 = find_last_by_elmininating_opposite(nelves)
