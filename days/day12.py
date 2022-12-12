from queue import Queue

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    grid, start, _ = parse(data)
    return bfs(grid, start, 'E')


def parse(data):
    grid = {(x, y): v for y, line in enumerate(data) for x, v in enumerate(line)}
    start = next(k for k, v in grid.items() if v == 'S')
    end = next(k for k, v in grid.items() if v == 'E')
    grid[start] = 'a'
    return grid, start, end


def bfs(grid, start, end):
    def check(dest, src):
        if end == 'a':
            dest, src = src, dest
        return grid[src] in 'yz' if grid[dest] == 'E' else ord(grid[dest]) <= ord(grid[src]) + 1

    q = Queue()
    q.put((start, 0))
    visited = {start}
    while not q.empty():
        cur_pos, cur_dist = q.get(block=False)

        if grid[cur_pos] == end:
            return cur_dist
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_pos = cur_pos[0] + dx, cur_pos[1] + dy
            if new_pos in grid and check(new_pos, cur_pos) and new_pos not in visited:
                q.put((new_pos, cur_dist + 1))
                visited.add(new_pos)


def part_two(data):
    grid, _, end = parse(data)
    return bfs(grid, end, 'a')


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
