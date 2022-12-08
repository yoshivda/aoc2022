import math

from lib import load_input


def solve(data):
    return part_one(data.splitlines())
    # return part_two(data.splitlines())


def part_one(data):
    trees = [[int(x) for x in line] for line in data]
    xmax, ymax = len(trees[0]), len(trees)
    return sum(sum(row) for row in [[(x in (0, len(trees[0]) - 1) or y in (0, ymax - 1)) or
                                     (x > 0 and max(trees[y][:x]) < trees[y][x]) or
                                     (x < len(trees[0]) - 1 and max(trees[y][x + 1:]) < trees[y][x]) or
                                     (y > 0 and max(trees[i][x] for i in range(y)) < trees[y][x]) or
                                     (y < len(trees) - 1 and max(trees[i][x] for i in range(y + 1, ymax)) < trees[y][x])
                                     for x in range(xmax)] for y in range(ymax)])


def part_two(data):
    trees = [[int(x) for x in line] for line in data]
    xmax, ymax = len(trees[0]), len(trees)
    res = [[0 for _ in range(len(trees[0]))] for _ in range(len(trees))]

    for y in range(1, ymax - 1):
        for x in range(1, xmax - 1):
            res[y][x] = math.prod(
                [count_dir(trees, x, y, dx, dy, xmax, ymax) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]])

    return max(max(row) for row in res)


def count_dir(trees, x, y, dx, dy, xmax, ymax):
    new_x, new_y = x + dx, y + dy
    count = 0
    while -1 < new_x < xmax and -1 < new_y < ymax:
        count += 1
        if trees[new_y][new_x] >= trees[y][x]:
            break
        new_x += dx
        new_y += dy

    return count


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
