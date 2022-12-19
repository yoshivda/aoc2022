from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    cubes = {tuple(map(int, line.split(','))) for line in data}
    return sum(len(neighbours(x, y, z) - cubes) for x, y, z in cubes)


def neighbours(x, y, z):
    return {(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)}


def part_two(data):
    cubes = {tuple(map(int, line.split(','))) for line in data}
    visited = set()
    minmax = tuple((min(c[i] for c in cubes), max(c[i] for c in cubes)) for i in range(3))
    gas = {(minmax[0][0] - 1, minmax[1][0] - 1, minmax[2][0] - 1)}
    res = 0
    while True:
        old_len = len(gas)
        new_gas = set()
        for g in gas:
            if g in visited:
                continue
            visited.add(g)
            for n in neighbours(*g):
                if n in gas:
                    continue
                elif n in cubes:
                    res += 1
                elif all(minmax[i][0] - 2 < n[i] <= minmax[i][1] + 2 for i in range(3)):
                    new_gas.add(n)
        gas |= new_gas
        if len(gas) == old_len:
            return res


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
