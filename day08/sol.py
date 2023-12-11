#!/usr/bin/env python3

import re
from pprint import pprint
import math as m


def load_input():
    data = list()
    instruction = None
    pattern = re.compile('(\w+) = \((\w+), (\w+)\)')
    with open('input') as fd:
        for i, line in enumerate(fd):
            line = line.strip()
            if i == 0:
                instruction = line
            elif line:
                match = pattern.search(line)
                src = match.group(1)
                dst = (match.group(2), match.group(3))
                data.append((src, dst))
            else:
                pass

    return instruction, data


def part1():
    graph = dict()
    instruction, data = load_input()
    for d in data:
        graph[d[0]] = {'L': d[1][0], 'R': d[1][1]}

    i = 0
    state = 'AAA'
    while True:
        c = instruction[i % len(instruction)]
        state = graph[state][c]
        i += 1
        if state == 'ZZZ':
            break

    result = i

    print("Result 1: ", result)


def part2():
    graph = dict()
    instruction, data = load_input()
    for d in data:
        graph[d[0]] = {'L': d[1][0], 'R': d[1][1]}

    i = 0
    states = [k for k in graph.keys() if k[-1] == 'A']

    ends = [list() for _ in range(6)]
    while True:
        c = instruction[i % len(instruction)]
        next_states = list()
        for state in states:
            next_states.append(graph[state][c])
        states = next_states
        i += 1
        for j in range(len(states)):
            if states[j][-1] == 'Z':
                ends[j].append(i)
        if i > 100000:
            break
    for end in ends:
        print(end[1] - end[0])

    # print(m.gcd(13201, 22411))
    values = (13201, 22411, 18727, 18113, 16271, 20569)
    # 307 is gcd of all numbers
    values_prime = [v//307 for v in values]

    result = m.prod(values_prime)*307

    print("Result 2: ", result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
