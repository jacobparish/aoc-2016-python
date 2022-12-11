from aocd import data
import hashlib
import utils


def get_neighbors_1(seed: str, path: str, x: int, y: int):
    u, d, l, r = hashlib.md5((seed + path).encode()).hexdigest()[:4]
    if y > 0 and u in "bcdef":
        yield (path + "U", x, y - 1)
    if y < 3 and d in "bcdef":
        yield (path + "D", x, y + 1)
    if x > 0 and l in "bcdef":
        yield (path + "L", x - 1, y)
    if x < 3 and r in "bcdef":
        yield (path + "R", x + 1, y)


dists1 = utils.shortest_paths(
    ("", 0, 0),
    lambda v: get_neighbors_1(data, *v),
    stop_condition=lambda dists: any(node[1:] == (3, 3) for node in dists),
)
p1 = next(node[0] for node in dists1 if node[1:] == (3, 3))


def get_neighbors_2(seed: str, path: str, x: int, y: int):
    if (x, y) != (3, 3):
        u, d, l, r = hashlib.md5((seed + path).encode()).hexdigest()[:4]
        if y > 0 and u in "bcdef":
            yield (path + "U", x, y - 1)
        if y < 3 and d in "bcdef":
            yield (path + "D", x, y + 1)
        if x > 0 and l in "bcdef":
            yield (path + "L", x - 1, y)
        if x < 3 and r in "bcdef":
            yield (path + "R", x + 1, y)


dists2 = utils.shortest_paths(("", 0, 0), lambda v: get_neighbors_2(data, *v))
p2 = max(dists2.values())
