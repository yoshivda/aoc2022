from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    head = tail = (0, 0)
    res = {(0, 0)}
    dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}
    for line in data:
        d, f = line.split()
        for _ in range(int(f)):
            dx, dy = dirs[d]
            head = (head[0] + dx, head[1] + dy)
            tail = move(head, tail)
            res.add(tail)
    return len(res)


def move(head, tail):
    diff_x, diff_y = head[0] - tail[0], head[1] - tail[1]
    if -1 <= diff_x <= 1 and -1 <= diff_y <= 1:
        return tail
    norm_diff_x = min(max(diff_x, -1), 1)
    norm_diff_y = min(max(diff_y, -1), 1)
    return tail[0] + norm_diff_x, tail[1] + norm_diff_y


def part_two(data):
    positions = [(0, 0) for _ in range(10)]
    res = {(0, 0)}
    dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}
    for line in data:
        d, f = line.split()
        dx, dy = dirs[d]
        for _ in range(int(f)):
            positions[0] = (positions[0][0] + dx, positions[0][1] + dy)
            for i in range(1, 10):
                positions[i] = move(positions[i - 1], positions[i])

            res.add(positions[9])
    return len(res)


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input('med')))
    print(solve(load_input()))
