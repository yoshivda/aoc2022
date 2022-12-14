from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    grid = {(500, 0): '+'}
    for line in data:
        points = line.split(' -> ')
        cur_x, cur_y = map(int, points[0].split(','))
        for i in range(1, len(points)):
            prev_x, prev_y = cur_x, cur_y
            cur_x, cur_y = map(int, points[i].split(','))
            if prev_x != cur_x:
                for x in range(min(prev_x, cur_x), max(prev_x, cur_x) + 1):
                    grid[(x, cur_y)] = '#'
            else:
                for y in range(min(prev_y, cur_y), max(prev_y, cur_y) + 1):
                    grid[(cur_x, y)] = '#'
    ymax = max(y for (_, y) in grid.keys())
    cnt = 0
    while True:
        x, y = 500, 1
        while True:
            if y >= ymax:
                return cnt
            if (x, y + 1) not in grid:
                y += 1
            elif (x - 1, y + 1) not in grid:
                x -= 1
                y += 1
            elif (x + 1, y + 1) not in grid:
                x += 1
                y += 1
            else:
                grid[(x, y)] = 'o'
                break
        cnt += 1


def part_two(data):
    grid = dict()
    for line in data:
        points = line.split(' -> ')
        cur_x, cur_y = map(int, points[0].split(','))
        for i in range(1, len(points)):
            prev_x, prev_y = cur_x, cur_y
            cur_x, cur_y = map(int, points[i].split(','))
            if prev_x != cur_x:
                for x in range(min(prev_x, cur_x), max(prev_x, cur_x) + 1):
                    grid[(x, cur_y)] = '#'
            else:
                for y in range(min(prev_y, cur_y), max(prev_y, cur_y) + 1):
                    grid[(cur_x, y)] = '#'
    ymax = max(y for (_, y) in grid.keys()) + 1
    cnt = 0
    while (500, 0) not in grid:
        x, y = 500, 0
        while True:
            if y == ymax:
                grid[(x, y)] = 'o'
                break
            elif (x, y + 1) not in grid:
                y += 1
            elif (x - 1, y + 1) not in grid:
                x -= 1
                y += 1
            elif (x + 1, y + 1) not in grid:
                x += 1
                y += 1
            else:
                grid[(x, y)] = 'o'
                break
        cnt += 1

    return cnt


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
