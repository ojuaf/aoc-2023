#!/usr/bin/env python3

import math as m


def load_input():
    data = list()
    with open('input') as fd:
        for i, line in enumerate(fd):
            temp = line.strip().split()
            temp = [int(t) for t in temp[1:]]
            data.append(temp)

    return data


def part1():
    data = load_input()
    wins = [0 for _ in range(len(data[0]))]
    j = 0
    for time, record in zip(data[0], data[1]):
        for i in range(time):
            dist = i*(time-i)
            if dist > record:
                wins[j] += 1
        j += 1
    result = m.prod(wins)

    print("Result 1: ", result)


def part2():
    time = 50748685
    record = 242101716911252
    wins = 0
    for i in range(time):
        dist = i*(time-i)
        if dist > record:
            wins += 1
    result = wins
    print("Result 2: ", result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
