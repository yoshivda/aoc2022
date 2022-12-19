import math
import re

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def exec_plan(plan_no, ore_ore, ore_clay, ore_obs, clay_obs, ore_geode, obs_geode, max_time):
    states = dict()

    def loop(ore_robots, clay_robots, obs_robots, ore, clay, obs, time):
        if time == 0:
            return 0
        state = (ore_robots, clay_robots, obs_robots, ore, clay, obs, time)
        if state in states:
            return states[state]

        options = []

        if ore >= ore_geode and obs >= obs_geode:
            options.append((0, 0, 0, -ore_geode, 0, -obs_geode, time - 1))

        if ore >= ore_obs and clay >= clay_obs and obs_robots < obs_geode and (ore - ore_robots < ore_obs or clay - clay_robots < clay_obs):
            options.append((0, 0, 1, -ore_obs, -clay_obs, 0))

        if ore - ore_robots < ore_clay <= ore and clay_robots < clay_obs:
            options.append((0, 1, 0, -ore_clay, 0, 0))

        if time > ore_ore + 1 and ore - ore_robots < ore_ore <= ore and ore_robots < max(ore_geode, ore_obs, ore_clay):
            options.append((1, 0, 0, -ore_ore, 0, 0))

        if len(options) < 4:
            options.append((0, 0, 0, 0, 0, 0))

        ore += ore_robots
        clay += clay_robots
        obs += obs_robots
        ore = min(ore, max(ore_geode, ore_obs, ore_clay) * time)
        clay = min(clay, clay_obs * time)
        obs = min(obs, obs_geode * time)
        new_state = (ore_robots, clay_robots, obs_robots, ore, clay, obs)

        res = max(loop(*(new_state[i] + option[i] for i in range(6)), time - 1) + (option[6] if len(option) == 7 else 0) for option in options)
        states[state] = res
        return res

    return loop(1, 0, 0, 0, 0, 0, max_time)


def part_one(data):
    plans = [list(map(int, re.findall(r'\d+', line))) for line in data]
    return sum((i + 1) * exec_plan(*plan, 32) for i, plan in enumerate(plans))


def part_two(data):
    plans = [list(map(int, re.findall(r'\d+', line))) for line in data]
    return math.prod(exec_plan(*plan, 32) for i, plan in enumerate(plans[:3]))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
