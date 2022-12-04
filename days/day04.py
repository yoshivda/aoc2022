from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return sum((nums := [int(x) for x in line.replace('-', ',').split(',')])[0] <= nums[2] <= nums[3] <= nums[1] or nums[2] <= nums[0] <= nums[1] <= nums[3] for line in data)


def part_two(data):
    return sum((nums := [int(x) for x in line.replace('-', ',').split(',')])[0] <= nums[3] and nums[1] >= nums[2] for line in data)


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
