import re

from lib import load_input


def solve(data):
    # return part_one(*data.split('\n\n'))
    return part_two(*data.split('\n\n'))


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def parse_grid(data):
    return {(x, y): c for y, line in enumerate(data.splitlines()) for x, c in enumerate(line) if c != ' '}


def part_one(grid, instr):
    def move(facing, steps, x, y, max_x, max_y):
        for _ in range(steps):
            new_pos = (x + directions[facing][0], y + directions[facing][1])
            if new_pos not in grid:
                if facing == 0:
                    new_pos = next((px, y) for px in range(x) if (px, y) in grid)
                elif facing == 1:
                    new_pos = next((x, py) for py in range(y) if (x, py) in grid)
                elif facing == 2:
                    new_pos = next((px, y) for px in range(max_x, x, -1) if (px, y) in grid)
                elif facing == 3:
                    new_pos = next((x, py) for py in range(max_y, y, -1) if (x, py) in grid)

            if grid[new_pos] == '.':
                x, y = new_pos
            else:
                break
        return x, y

    grid = parse_grid(grid)
    max_x = max(x for (x, _) in grid.keys())
    max_y = max(y for (_, y) in grid.keys())
    x, y = next((x, 0) for x in range(max_x + 1) if (x, 0) in grid)
    facing = 0
    steps = list(map(int, re.findall(r'\d+', instr)))
    turns = re.findall('[L|R]', instr)
    for i in range(len(turns)):
        # print_grid(grid, max_x, max_y)
        x, y = move(facing, steps[i], x, y, max_x, max_y)
        facing = (facing + 1 if turns[i] == 'R' else facing - 1) % 4
    x, y = move(facing, steps[-1], x, y, max_x, max_y)
    return (y + 1) * 1000 + (x + 1) * 4 + facing


def part_two(grid, instr):
    def move(facing, steps, x, y):
        for _ in range(steps):
            new_x = x + directions[facing][0]
            new_y = y + directions[facing][1]
            old_facing = facing
            if (new_x, new_y) not in grid:
                if 50 <= x < 100 and 0 <= y < 50:
                    if facing == 2:
                        new_y = 149 - y
                    elif facing == 3:
                        new_y = x + 100
                    facing = 0
                    new_x = 0

                elif 100 <= x < 150 and 0 <= y < 50:
                    if facing == 0:
                        new_y = 149 - y
                    elif facing == 1:
                        new_y = x - 50

                    if facing == 3:
                        new_y = 199
                        new_x = x - 100
                    else:
                        new_x = 99
                        facing = 2

                elif 50 <= x < 100 and 50 <= y < 100:
                    if facing == 0:
                        new_x = y + 50
                        new_y = 49
                    elif facing == 2:
                        new_x = y - 50
                        new_y = 100
                    facing = (facing - 1) % 4

                elif 50 <= x < 100 and 100 <= y < 150:
                    if facing == 0:
                        facing = 2
                        new_x = 149
                        new_y = 149 - y
                    elif facing == 1:
                        new_y = x + 100
                        new_x = 49
                        facing = 2

                elif 0 <= x < 50 and 100 <= y < 150:
                    if facing == 2:
                        new_y = 149 - y
                    elif facing == 3:
                        new_y = x + 50
                    facing = 0
                    new_x = 50

                elif 0 <= x < 50 and 150 <= y < 200:
                    if facing == 0:
                        new_x = y - 100
                        new_y = 149
                        facing = 3
                    elif facing == 1:
                        new_y = 0
                        new_x = x + 100
                    elif facing == 2:
                        new_x = y - 100
                        new_y = 0
                        facing = 1

            if grid[(new_x, new_y)] == '.':
                x, y = new_x, new_y
            else:
                facing = old_facing
                break
        return x, y, facing

    grid = parse_grid(grid)
    max_x = max(x for (x, _) in grid)
    x, y = next((x, 0) for x in range(max_x + 1) if (x, 0) in grid)
    facing = 0
    steps = list(map(int, re.findall(r'\d+', instr)))
    turns = re.findall('[L|R]', instr)
    for i in range(len(turns)):
        x, y, facing = move(facing, steps[i], x, y)
        facing = (facing + 1 if turns[i] == 'R' else facing - 1) % 4
    x, y, facing = move(facing, steps[-1], x, y)
    return (y + 1) * 1000 + (x + 1) * 4 + facing


if __name__ == '__main__':
    # print(solve(load_input('small')))  # does not work for part 2 due to different shape
    print(solve(load_input()))
