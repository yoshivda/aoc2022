from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    blizzards = tuple((x - 1, y - 1, c) for y, line in enumerate(data) for x, c in enumerate(line) if c in '><v^')
    start = (data[0].index('.') - 1, 0)
    end = (data[-1].index('.') - 1, len(data) - 2)
    xmax = len(data[0]) - 2
    ymax = len(data) - 2
    return bfs(start, end, blizzards, xmax, ymax)[0]


def neighbours(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def bfs(start, end, blizzards, xmax, ymax):
    elves = {start}
    dist = 0

    while True:
        dist += 1
        blizzards, bliz_set = update_blizzards(blizzards, xmax, ymax)
        new_elves = set()
        for cur in elves:
            for nx, ny in neighbours(*cur):
                if (nx, ny) == end:
                    return dist, blizzards
                if (nx, ny) not in bliz_set and 0 <= nx < xmax and 0 <= ny < ymax:
                    new_elves.add((nx, ny))
            if cur not in bliz_set:
                new_elves.add(cur)
        elves = new_elves


def update_blizzards(blizzards, xmax, ymax):
    res = []
    for x, y, c in blizzards:
        if c == '>':
            x += 1
        elif c == '<':
            x -= 1
        elif c == '^':
            y -= 1
        elif c == 'v':
            y += 1
        x %= xmax
        y %= ymax
        res.append((x, y, c))
    return tuple(res), {(x, y) for x, y, _ in res}


def part_two(data):
    blizzards = tuple((x - 1, y - 1, c) for y, line in enumerate(data) for x, c in enumerate(line) if c in '><v^')
    start = (data[0].index('.') - 1, 0)
    end = (data[-1].index('.') - 1, len(data) - 2)
    xmax = len(data[0]) - 2
    ymax = len(data) - 2
    a, blizzards = bfs(start, end, blizzards, xmax, ymax)
    b, blizzards = bfs(end, start, blizzards, xmax, ymax)
    c, _ = bfs(start, end, blizzards, xmax, ymax)
    return a + b + c


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
