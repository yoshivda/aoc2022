from __future__ import annotations

import heapq
import math
from dataclasses import dataclass

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


@dataclass
class Monkey:
    items: list[int]
    operation: str
    test_num: int
    test_res: tuple[int, int]
    monkeys: list[Monkey]
    inspections: int = 0
    lcm: int = 0

    def take_turn(self, divide):
        self.inspections += len(self.items)
        for old in self.items:
            new = eval(self.operation)
            if divide:
                new //= 3
            new %= self.lcm
            self.monkeys[self.test_res[new % self.test_num != 0]].items.append(new)

        self.items = []


def parse(data):
    monkeys: list[Monkey] = []
    for i in range(1, len(data), 7):
        items = list(map(int, data[i][data[i].index(':') + 2:].split(', ')))
        operation = data[i + 1][data[i + 1].index('=') + 2:]
        test_num, *test_res = (int(data[i + y].split()[-1]) for y in range(2, 5))
        monkeys.append(Monkey(items, operation, test_num, test_res, monkeys))
    lcm = math.lcm(*[m.test_num for m in monkeys])
    for m in monkeys:
        m.lcm = lcm
    return monkeys


def part_one(data: list[str]):
    monkeys = parse(data)

    for _ in range(20):
        for m in monkeys:
            m.take_turn(True)

    return math.prod(heapq.nlargest(2, [m.inspections for m in monkeys]))


def part_two(data):
    monkeys = parse(data)

    for x in range(10000):
        for m in monkeys:
            m.take_turn(False)

    return math.prod(heapq.nlargest(2, [m.inspections for m in monkeys]))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
