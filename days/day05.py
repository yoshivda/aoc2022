from collections import defaultdict

from lib import load_input


def solve(data):
    # return part_one(*data.split('\n\n'))
    return part_two(*data.split('\n\n'))


def read_stacks(data):
    stacks = defaultdict(list)
    for line in data.splitlines():
        if line.startswith(' 1'):
            break
        for i in range(1, len(line), 4):
            if char := line[i].strip():
                stacks[(i - 1) // 4 + 1].append(char)
    for k, v in stacks.items():
        stacks[k] = list(reversed(v))
    return stacks


def part_one(grid, instr):
    stacks = read_stacks(grid)

    for line in instr.splitlines():
        _, times, _, src, _, dest = line.split()
        for _ in range(int(times)):
            stacks[int(dest)].append(stacks[int(src)].pop())

    return ''.join((v[-1] for _, v in sorted(stacks.items())))


def part_two(grid, instr):
    stacks = read_stacks(grid)

    for line in instr.splitlines():
        _, times, _, src, _, dest = line.split()
        stacks[int(dest)].extend(stacks[int(src)][-int(times):])
        stacks[int(src)] = stacks[int(src)][:-int(times)]
    
    return ''.join((v[-1] for _, v in sorted(stacks.items())))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
