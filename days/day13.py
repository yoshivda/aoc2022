import functools
import math

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def compare(one, two):
    if isinstance(one, int) and isinstance(two, int):
        return -1 if one < two else 0 if one == two else 1
    if not isinstance(one, list):
        one = [one]
    if not isinstance(two, list):
        two = [two]
    for i in range(len(one)):
        if i >= len(two):
            return 1
        if (cmp := compare(one[i], two[i])) != 0:
            return cmp
    if len(one) < len(two):
        return -1
    return 0


def part_one(data):
    return sum(i // 3 + 1 for i in range(0, len(data), 3) if compare(eval(data[i]), eval(data[i + 1])) == -1)


def part_two(data):
    extra = [[[2]], [[6]]]
    evaluated = sorted([eval(data[i]) for i in range(len(data)) if (i + 1) % 3 != 0] + extra, key=functools.cmp_to_key(compare))
    return math.prod(evaluated.index(e) + 1 for e in extra)


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
