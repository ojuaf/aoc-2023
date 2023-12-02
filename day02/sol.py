#!/usr/bin/env python3


def load_input():
    with open('input') as fd:
        data = list()
        for line in fd:
            line = line.strip()
            _, games = line.split(':')
            rounds = games.strip().split(';')
            temp = list()
            for r in rounds:
                draws = r.strip().split(',')
                for draw in draws:
                    number, color = draw.strip().split(' ')
                    temp.append((int(number), color))

            data.append(temp)
    return data


def part1():
    limit = {'red': 12, 'green': 13, 'blue': 14}

    data = load_input()
    result = 0
    for i, r in enumerate(data):
        possible = True
        for a in r:
            if limit[a[1]] < a[0]:
                possible = False
                break

        if possible:
            result += 1+i

    print("Result 1: ", result)


def part2():
    data = load_input()

    result = 0
    for r in data:
        limit = {'red': 0, 'green': 0, 'blue': 0}
        for a in r:
            limit[a[1]] = max(a[0], limit[a[1]])

        temp = 1
        for v in limit.values():
            temp *= v
        result += temp

    print("Result 2: ", result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
