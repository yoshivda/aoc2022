from lib import load_input


def solve(data):
    rocks = parse_rocks(load_input('rocks'))
    # return part_one(data.strip(), rocks)
    return part_two(data.strip(), rocks)


def parse_rocks(data):
    rocks = []
    for group in data.split('\n\n'):
        rock = set()
        group = group.splitlines()
        for i, line in enumerate(group):
            for j, char in enumerate(line):
                if char == '#':
                    rock.add((j, len(group) - 1 - i))
        rocks.append(rock)
    return rocks


def part_one(data, rocks):
    j = height = 0
    occupied = set()
    for i in range(2022):
        rock = rocks[i % len(rocks)]
        x = 2
        y = height + 3
        while True:
            if data[j % len(data)] == '<' and x > 0 and all((gx + x - 1, gy + y) not in occupied for gx, gy in rock):
                x -= 1
            elif data[j % len(data)] == '>' and x + max(gx for gx, _ in rock) < 6 and all((gx + x + 1, gy + y) not in occupied for gx, gy in rock):
                x += 1
            j += 1

            if all((gx + x, gy + y - 1) not in occupied for gx, gy in rock) and y > 0:
                y -= 1
            else:
                rock_coords = {(x + gx, y + gy) for gx, gy in rock}
                occupied |= rock_coords
                height = max(height, max(ry for _, ry in rock_coords) + 1)
                break
    return height


def part_two(data, rocks):
    j = height = 0
    grid = [[False for _ in range(7)] for _ in range(500_000)]
    heights = []
    js = []
    for i in range(100_000):
        rock = rocks[i % len(rocks)]
        x = 2
        y = height + 3
        while True:
            if data[j % len(data)] == '<' and x > 0 and all(not grid[gy + y][gx + x - 1] for gx, gy in rock):
                x -= 1
            elif data[j % len(data)] == '>' and x + max(gx for gx, _ in rock) < 6 and all(not grid[gy + y][gx + x + 1] for gx, gy in rock):
                x += 1
            j += 1

            if all(not grid[gy + y - 1][gx + x] for gx, gy in rock) and y > 0:
                y -= 1
            else:
                rock_coords = {(x + gx, y + gy) for gx, gy in rock}
                for rx, ry in rock_coords:
                    grid[ry][rx] = True
                height = max(height, max(ry for _, ry in rock_coords) + 1)
                heights.append(height)
                js.append(j % len(data))
                break

    for i in range(2022, 100_000):
        for j in range(i + 1, 100_000):
            hi = heights[i]
            hj = heights[j]
            if i % len(rocks) == j % len(rocks) and js[i] == js[j] and grid[hi - 20:hi] == grid[hj - 20:hj]:
                period = j - i
                period_height = hj - hi
                cycles = (1000000000000 - i) // period
                remainder = (1000000000000 - i) % period
                return period_height * cycles + hi + heights[remainder + j] - hj - 1


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
