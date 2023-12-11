#!/usr/bin/env python3


def load_input():
    data = list()
    with open('input') as fd:
        for y, line in enumerate(fd):
            for x, i in enumerate(line.strip()):
                if i == '#':
                    data.append((y, x))

    return data


def part1():
    data = load_input()
    rows = set([y for y, x in data])
    cols = set([x for y, x in data])
    result = 0
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            a = data[i]
            b = data[j]
            y_spaces = sum([1 for y in range(min(b[0], a[0]), max(b[0], a[0])) if y not in rows])
            x_spaces = sum([1 for x in range(min(b[1], a[1]), max(b[1], a[1])) if x not in cols])
            dist = (y_spaces + x_spaces)*2 + abs(b[0]-a[0]) + abs(b[1]-a[1]) - x_spaces - y_spaces
            result += dist

    print("Result 1: ", result)


def part2():
    data = load_input()
    rows = set([y for y, x in data])
    cols = set([x for y, x in data])
    result = 0
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            a = data[i]
            b = data[j]
            y_spaces = sum([1 for y in range(min(b[0], a[0]), max(b[0], a[0])) if y not in rows])
            x_spaces = sum([1 for x in range(min(b[1], a[1]), max(b[1], a[1])) if x not in cols])
            dist = (y_spaces + x_spaces)*1000000 + abs(b[0]-a[0]) + abs(b[1]-a[1]) - x_spaces - y_spaces
            result += dist

    print("Result 2: ", result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
