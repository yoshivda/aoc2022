from lib import load_input


def solve(data):
    # return '\n'.join(str(part_one(line)) for line in data.splitlines())
    return '\n'.join(str(part_two(line)) for line in data.splitlines())


def part_one(data):
    return next(i for i in range(4, len(data)) if len(set(data[i-4:i])) == 4)


def part_two(data):
    return next(i for i in range(14, len(data)) if len(set(data[i-14:i])) == 14)


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
