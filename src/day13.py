from aocd import data
import utils


def is_wall(seed: int, x: int, y: int) -> bool:
    return utils.bitsum(seed + x * x + 3 * x + 2 * x * y + y + y * y) % 2 == 1


def get_neighbors(seed: int, x: int, y: int):
    if not is_wall(seed, x + 1, y):
        yield (x + 1, y)
    if not is_wall(seed, x, y + 1):
        yield (x, y + 1)
    if x > 0 and not is_wall(seed, x - 1, y):
        yield (x - 1, y)
    if y > 0 and not is_wall(seed, x, y - 1):
        yield (x, y - 1)


seed = int(data)
p1 = utils.shortest_path((1, 1), (31, 39), lambda v: get_neighbors(seed, *v))
p2 = len(utils.shortest_paths((1, 1), None, lambda v: get_neighbors(seed, *v), 50))
