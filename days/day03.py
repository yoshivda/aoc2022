import string

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return sum(string.ascii_letters.index((set(line[:len(line)//2]) & set(line[len(line)//2:])).pop()) + 1 for line in data)


def part_two(data):
    return sum(string.ascii_letters.index((set(data[x]) & set(data[x+1]) & set(data[x+2])).pop()) + 1 for x in range(0, len(data), 3))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
