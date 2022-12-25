from lib import load_input


def solve(data):
    return int_to_snafu(sum(snafu_to_int(line) for line in data.splitlines()))


def snafu_to_int(snafu):
    return sum(pow(5, i) * ('=-012'.index(c) - 2) for i, c in enumerate(reversed(snafu)))


def int_to_snafu(num):
    res = ''
    carry = 0
    while num or carry:
        cur = num % 5 + carry
        carry = 0
        if cur > 2:
            carry = 1
            cur %= 5
        res = (str(cur) if cur < 3 else '=' if cur == 3 else '-') + res
        num //= 5
    return res


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
