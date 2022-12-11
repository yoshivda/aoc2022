from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    x = i = 1
    res = []
    for line in data:
        if line.startswith('addx'):
            i += 1
            if (i + 20) % 40 == 0:
                res.append(x * i)
            x += int(line.split()[1])
        i += 1
        if (i + 20) % 40 == 0:
            res.append(x * i)
    return sum(res)


def print_step(i, x):
    if abs(x - (i % 40)) <= 1:
        print('█', end='')
    else:
        print(' ', end='')

    if (i + 1) % 40 == 0:
        print()


def part_two(data):
    x = 1
    i = 0
    for line in data:
        print_step(i, x)
        i += 1

        if line.startswith('addx'):
            print_step(i, x)
            i += 1
            x += int(line.split()[1])


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
