from collections import Counter
from functools import cache

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    elves = {(x, y) for y, line in enumerate(data) for x, c in enumerate(line) if c == '#'}
    elves = {t: i for i, t in enumerate(elves)}
    move_index = 0
    for _ in range(10):
        targets = dict()
        for (x, y), i in elves.items():
            options = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
            nbs = around(x, y)
            if len({x for nb in nbs for x in nb} & set(elves.keys())) == 0:
                continue
            for di in range(4):
                if len(set(elves.keys()) & nbs[(move_index + di) % 4]) == 0:
                    targets[(x, y)] = options[(move_index + di) % 4]
                    break
        move_index = (move_index + 1) % 4
        freq = Counter(targets.values())
        elves = {(targets[pos] if pos in targets and freq[targets[pos]] == 1 else pos): i for pos, i in elves.items()}
        xmin = min(x for (x, _) in elves)
        xmax = max(x for (x, _) in elves)
        ymin = min(y for (_, y) in elves)
        ymax = max(y for (_, y) in elves)
    return (xmax - xmin + 1) * (ymax - ymin + 1) - len(elves)


@cache
def around(x, y):
    return {(x + i, y - 1) for i in range(-1, 2)},\
           {(x + i, y + 1) for i in range(-1, 2)},\
           {(x - 1, y + i) for i in range(-1, 2)},\
           {(x + 1, y + i) for i in range(-1, 2)}


def part_two(data):
    elves = {(x, y) for y, line in enumerate(data) for x, c in enumerate(line) if c == '#'}
    elves = {t: i for i, t in enumerate(elves)}
    move_index = 0
    round = 0
    moves = True
    while moves:
        moves = False
        round += 1
        targets = dict()
        for (x, y), i in elves.items():
            options = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
            nbs = around(x, y)
            if all(x not in elves for nb in nbs for x in nb):
                continue
            moves = True
            for di in range(4):
                if all(nb not in elves for nb in nbs[(move_index + di) % 4]):
                    targets[(x, y)] = options[(move_index + di) % 4]
                    break
        move_index = (move_index + 1) % 4
        freq = Counter(targets.values())
        elves = {(targets[pos] if pos in targets and freq[targets[pos]] == 1 else pos): i for pos, i in elves.items()}
    return round


if __name__ == '__main__':
    # print(solve(load_input('mini')))
    print(solve(load_input('small')))
    print(solve(load_input()))
