from __future__ import annotations

from dataclasses import dataclass, field

from lib import load_input


@dataclass
class File:
    name: str
    size: int


@dataclass
class Dir:
    name: str
    parent: Dir | None
    contents: dict[str, File | Dir] = field(default_factory=dict)

    @property
    def size(self):
        return sum(c.size for c in self.contents.values())


def parse_input(data):
    root = Dir('/', None)
    cur = root
    it = iter(data)
    next(it)
    line: str = next(it)
    try:
        while True:
            if line.startswith('$ ls'):
                line = next(it)
                while not line.startswith('$'):
                    thing, name = line.split()
                    if thing == 'dir':
                        cur.contents[name] = Dir(name, cur)
                    else:
                        cur.contents[name] = File(name, int(thing))
                    line = next(it)
            elif line.startswith('$ cd'):
                if line[5:] == '..':
                    cur = cur.parent
                else:
                    cur = cur.contents[line[5:]]
                line = next(it)
    except StopIteration:
        return root


def traverse(structure, func) -> list:
    res = [func(structure)]
    if isinstance(structure, Dir):
        for child in structure.contents.values():
            res.extend(traverse(child, func))
    return res


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    structure = parse_input(data)
    return sum(traverse(structure, lambda item: item.size if isinstance(item, Dir) and item.size <= 100_000 else 0))


def part_two(data):
    structure = parse_input(data)
    req_size = 30000000 - (70000000 - structure.size)
    return min(traverse(structure, lambda item: item.size if isinstance(item, Dir) and item.size >= req_size else 999999999999))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
