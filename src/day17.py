from aocd import data
import hashlib
import utils


def get_neighbors(seed: str, path: str, x: int, y: int):
    if (x, y) == (3, 3):
        return
    u, d, l, r = hashlib.md5((seed + path).encode()).hexdigest()[:4]
    if y > 0 and u in "bcdef":
        yield (path + "U", x, y - 1)
    if y < 3 and d in "bcdef":
        yield (path + "D", x, y + 1)
    if x > 0 and l in "bcdef":
        yield (path + "L", x - 1, y)
    if x < 3 and r in "bcdef":
        yield (path + "R", x + 1, y)


dists = utils.shortest_paths(("", 0, 0), lambda v: get_neighbors(data, *v))
p1 = min((v for v in dists if v[1:] == (3, 3)), key=dists.get)[0]
p2 = max(dists.values())
