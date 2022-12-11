from aocd import lines
import itertools as it
import utils
from typing import List


def get_neighbors(grid: List[str], x: int, y: int):
    if x > 0 and grid[y][x - 1] != "#":
        yield (x - 1, y)
    if x < len(grid[0]) - 1 and grid[y][x + 1] != "#":
        yield (x + 1, y)
    if y > 0 and grid[y - 1][x] != "#":
        yield (x, y - 1)
    if y < len(grid) - 1 and grid[y + 1][x] != "#":
        yield (x, y + 1)


grid = lines
marked_locations = {}
marked_dists = {}

for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val not in ".#":
            marked_locations[val] = (x, y)

for id1, pos1 in marked_locations.items():
    dists = utils.shortest_paths(pos1, lambda v: get_neighbors(grid, *v))
    marked_dists.update(
        {(id1, id2): dists[pos2] for id2, pos2 in marked_locations.items()}
    )

start = marked_locations.pop("0")
p1 = min(
    sum(marked_dists[id1, id2] for id1, id2 in zip(("0", *perm), perm))
    for perm in it.permutations(marked_locations.keys())
)
p2 = min(
    sum(marked_dists[id1, id2] for id1, id2 in zip(("0", *perm), (*perm, "0")))
    for perm in it.permutations(marked_locations.keys())
)
