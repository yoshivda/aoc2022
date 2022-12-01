from lib import load_input


def solve(data):
    # return part_one(data.split('\n\n'))
    return part_two(data.split('\n\n'))


def part_one(data):
    return max(sum(int(x) for x in group.splitlines()) for group in data)


def part_two(data):
    return sum(sorted((sum(int(x) for x in group.splitlines()) for group in data), reverse=True)[:3])


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
