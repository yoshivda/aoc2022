import math

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


class Node:
    def __init__(self, name, *args):
        self.name = name
        self.val = int(args[0]) if len(args) == 1 else None
        if len(args) > 1:
            self.left, self.op, self.right = args

    def str(self, nodes):
        if self.val:
            return str(self.val)
        return f'({nodes[self.left].str(nodes)} {self.op} {nodes[self.right].str(nodes)})'


def parse_line(line):
    name = line.split(':')[0]
    split = line.split()[1:]
    return Node(name, *split)


def part_one(data):
    nodes = {(node := parse_line(line)).name: node for line in data}
    return int(eval(nodes['root'].str(nodes)))


def part_two(data):
    nodes = {(node := parse_line(line)).name: node for line in data}
    nodes['humn'].val = 'HUMN'
    nodes['root'].op = '-'

    low = 0
    high = int(1e16)
    orig = nodes['root'].str(nodes)
    while low <= high:
        cur = (low + high) // 2
        eq = orig.replace('HUMN', str(cur))
        res = eval(eq)
        if res < 0 if len(orig) < 50 else res > 0:
            low = cur + 1
        elif res == 0:
            return cur
        else:
            high = cur - 1


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
