#!/usr/bin/env python3


def load_input():
    with open('input') as fd:
        data = list()
        for line in fd:
            line = line.strip()
            data.append(line)
    return data


def get_neighbors_position(data, y, x):
    pos = list()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= y+i < len(data) and 0 <= x+j < len(data[0]):
                if i != 0 or j != 0:
                    pos.append((y+i, x+j))

    return pos


def part1():
    data = load_input()
    numbers = list()
    symbol = None
    number = ""
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j].isdigit():
                number += data[i][j]
                neighbors = [data[i+k][j+m] for k in range(-1, 2)
                             for m in range(-1, 2) if 0 <= i+k < len(data) and
                             0 <= j+m < len(data[0])]
                for n in neighbors:
                    if not n.isdigit() and n != '.':
                        symbol = n
            elif number:
                numbers.append((int(number), symbol))
                number = ""
                symbol = None
            else:
                pass

    result = sum([n[0] for n in numbers if n[1] is not None])

    print("Result 1: ", result)


def part2():
    data = load_input()
    numbers = list()
    symbol = None
    number = ""
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j].isdigit():
                number += data[i][j]
                neighbor_pos = get_neighbors_position(data, i, j)
                for y, x in neighbor_pos:
                    if data[y][x] == '*':
                        symbol = (y, x)
            elif number:
                if symbol is not None:
                    numbers.append((int(number), symbol))
                number = ""
                symbol = None
            else:
                pass

    positions = [n[1] for n in numbers]
    result = 0
    for i in range(len(positions)):
        if positions.count(positions[i]) == 2:
            a = i
            try:
                b = positions.index(positions[i], i+1)
                result += numbers[a][0] * numbers[b][0]
            except Exception:
                pass

    print("Result 2: ", result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
