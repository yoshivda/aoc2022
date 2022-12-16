import re
from functools import cache

from lib import load_input

valves = dict()


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    for line in data:
        flow = int(re.search(r'\d+', line).group())
        current, *to = re.findall(r'[A-Z]{2}', line)
        valves[current] = (flow, to)
    return best_value('AA', frozenset(), 30, len(data))


@cache
def best_value(cur, opened, time, part):
    if time <= 0:
        return 0
    return max(valves[cur][0] * (time - 1) + max(best_value(nb, frozenset(opened | {cur}), time - 2, part) for nb in valves[cur][1]) if cur not in opened and valves[cur][0] > 0 else 0,
               max(best_value(nb, opened, time - 1, part) for nb in valves[cur][1]) if time > 2 else 0)


def part_two(data):
    for line in data:
        flow = int(re.search(r'\d+', line).group())
        current, *to = re.findall(r'[A-Z]{2}', line)
        valves[current] = (flow, to)
    return best_value_two('AA', frozenset(), 26, len(data))


@cache
def best_value_two(cur, opened, time, part):
    if time <= 0:
        return 0
    return max(valves[cur][0] * (time - 1) + max(best_value_two(nb, frozenset(opened | {cur}), time - 2, part) for nb in valves[cur][1]) if cur not in opened and valves[cur][0] > 0 else 0,
               max(best_value_two(nb, opened, time - 1, part) for nb in valves[cur][1]) if time > 2 else 0,
               best_value('AA', frozenset(opened | {cur}), 26, part) + valves[cur][0] * (time - 1) if cur not in opened and valves[cur][0] > 0 else best_value('AA', opened, 26, part))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
