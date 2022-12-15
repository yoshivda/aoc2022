import re

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    if len(data) == 14:  # Sample input
        target = 10
    else:  # Actual input
        target = 2_000_000
    occupied = set()
    beacons = set()
    for line in data:
        sx, sy, bx, by = map(int, re.findall(r'=(-?\d+)', line))
        if by == target:
            beacons.add(bx)
        dist = distance(sx, sy, bx, by)
        if abs(sy - target) > dist:
            continue
        for x in range(sx - (dist - abs(sy - target)), sx + (dist - abs(sy - target)) + 1):
            occupied.add(x)
    return len(occupied - beacons)


def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def part_two(data):
    if len(data) == 14:  # Sample input
        cmax = 20
    else:  # Actual input
        cmax = 4000000
    sensors = set()
    for line in data:
        sx, sy, bx, by = map(int, re.findall(r'=(-?\d+)', line))
        sensors.add((sx, sy, distance(sx, sy, bx, by)))
    for sx, sy, dist in sensors:
        for x, y in perimeter(sx, sy, dist + 1, cmax):
            if all(distance(x, y, psx, psy) > pdist for psx, psy, pdist in sensors):
                return x * 4000000 + y


def perimeter(x, y, dist, cmax):
    cur_x = x
    cur_y = y + dist
    if 0 <= cur_x <= cmax and 0 <= cur_y <= cmax:
        yield cur_x, cur_y

    while cur_y != y:
        cur_y -= 1
        cur_x -= 1
        if 0 <= cur_x <= cmax and 0 <= cur_y <= cmax:
            yield cur_x, cur_y

    while cur_x != x:
        cur_y -= 1
        cur_x += 1
        if 0 <= cur_x <= cmax and 0 <= cur_y <= cmax:
            yield cur_x, cur_y

    while cur_y != y:
        cur_y += 1
        cur_x += 1
        if 0 <= cur_x <= cmax and 0 <= cur_y <= cmax:
            yield cur_x, cur_y

    while cur_x != x:
        cur_y += 1
        cur_x -= 1
        if 0 <= cur_x <= cmax and 0 <= cur_y <= cmax:
            yield cur_x, cur_y


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
