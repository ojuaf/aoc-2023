#!/usr/bin/env python3

import math as m


def load_input():
    data = list()
    with open('input') as fd:
        for line in fd:
            temp = line.strip().split()
            temp = [int(t) for t in temp]
            data.append(temp)

    return data


def part2():
    data = load_input()
    diffs = list()
    result = 0
    for d in data:
        diffs = list()
        diffs.append(d)
        while True:
            diff = [diffs[-1][i+1]-diffs[-1][i] for i in range(len(diffs[-1])-1)]
            diffs.append(diff)
            if not any(diff):
                size = len(diffs)
                value = 0
                for j in range(len(diffs)-1):
                    value = diffs[size-j-2][0] - value
                else:
                    result += value
                break
    result = result

    print("Result 2: ", result)


def part1():
    data = load_input()
    diffs = list()
    result = 0

    for d in data:
        diffs = list()
        diffs.append(d)
        while True:
            diff = [diffs[-1][i+1]-diffs[-1][i] for i in range(len(diffs[-1])-1)]
            diffs.append(diff)
            if not any(diff):
                size = len(diffs)
                value = 0
                for j in range(len(diffs)-1):
                    value += diffs[size-j-2][-1]
                else:
                    result += value
                break
    result = result

    print("Result 1: ", result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
