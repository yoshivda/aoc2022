from lib import load_input


def solve(data):
    # return part_one(list(map(int, data.splitlines())))
    return part_two(list(map(int, data.splitlines())))


def part_one(data):
    orig = list(enumerate(data))
    actual = orig[:]
    for (orig_i, v) in orig:
        actual_i = actual.index((orig_i, v))
        actual.insert((actual_i + v) % (len(actual) - 1), actual.pop(actual_i))
    zero = (data.index(0), 0)
    return sum(actual[(actual.index(zero) + i * 1000) % len(actual)][1] for i in range(1, 4))


def part_two(data):
    orig = list(enumerate(x * 811589153 for x in data))
    actual = orig[:]
    for _ in range(10):
        for (orig_i, v) in orig:
            actual_i = actual.index((orig_i, v))
            actual.insert((actual_i + v) % (len(actual) - 1), actual.pop(actual_i))
    zero = (data.index(0), 0)
    return sum(actual[(actual.index(zero) + i * 1000) % len(actual)][1] for i in range(1, 4))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
