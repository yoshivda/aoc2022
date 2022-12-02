from lib import load_input


def solve(data):
    # return part_one(data)
    return part_two(data)


def part_one(data):
    return sum(ord(line[2]) - 87 + (6 if 'ABC'['ABC'.index(chr(ord(line[2]) - 23)) - 1] == line[0] else 3 if line[0] == chr(ord(line[2]) - 23) else 0) for line in data.splitlines())


def part_two(data):
    return sum((ord(line[2]) - 88) * 3 + (ord(line[0]) + ord(line[2]) - 154) % 3 + 1 for line in data.splitlines())


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
