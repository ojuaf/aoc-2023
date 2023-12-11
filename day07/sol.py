#!/usr/bin/env python3

import math as m
from functools import cmp_to_key


map_pictures = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

map_pictures_2 = {
    'T': 10,
    'J': 0,
    'Q': 12,
    'K': 13,
    'A': 14,
}


map_types = {
    'high': 0,
    'two': 1,
    'double': 2,
    'three': 3,
    'full': 4,
    'four': 5,
    'five': 6,
}


def load_input():
    data = list()
    with open('input') as fd:
        for line in fd:
            temp = line.strip().split()
            conv_hand = list()
            for h in temp[0]:
                conv_hand.append(map_pictures[h] if h in map_pictures else int(h))
            data.append([conv_hand, int(temp[1])])

    return data


def load_input_2():
    data = list()
    with open('input') as fd:
        for line in fd:
            temp = line.strip().split()
            conv_hand = list()
            for h in temp[0]:
                conv_hand.append(map_pictures_2[h] if h in map_pictures else int(h))
            data.append([conv_hand, int(temp[1])])

    return data


def find_type(hand):
    """"""
    kinds = set(hand)
    numbers = list()
    for k in kinds:
        numbers.append(hand.count(k))

    type = None
    if 5 in numbers:
        type = 'five'
    elif 4 in numbers:
        type = 'four'
    elif 3 in numbers:
        if 2 in numbers:
            type = 'full'
        else:
            type = 'three'
    elif 2 in numbers:
        if numbers.count(2) == 2:
            type = 'double'
        else:
            type = 'two'
    else:
        type = 'high'
    return type


def find_type_2(hand):
    """"""
    kinds = set(hand)
    jokers = hand.count(0)

    numbers = list()
    for k in kinds:
        if k != 0:
            numbers.append(hand.count(k))

    if not numbers:
        numbers.append(0)
    numbers[numbers.index(max(numbers))] += jokers

    type = None
    if 5 in numbers:
        type = 'five'
    elif 4 in numbers:
        type = 'four'
    elif 3 in numbers:
        if 2 in numbers:
            type = 'full'
        else:
            type = 'three'
    elif 2 in numbers:
        if numbers.count(2) == 2:
            type = 'double'
        else:
            type = 'two'
    else:
        type = 'high'
    return type


def compare(x, y):
    result = 0
    if x[2] > y[2]:
        result = 1
    elif x[2] < y[2]:
        result = -1
    else:
        for i, j in zip(x[0], y[0]):
            if i > j:
                result = 1
                break
            elif i < j:
                result = -1
                break
            else:
                pass

    return result


def part1():
    data = load_input()

    for i, d in enumerate(data):
        type = find_type(d[0])
        data[i].append(map_types[type])

    ranks = sorted(data, key=cmp_to_key(compare))
    result = 0
    for i, r in enumerate(ranks):
        result += (i+1)*r[1]

    print("Result 1: ", result)


def part2():
    data = load_input_2()

    for i, d in enumerate(data):
        type = find_type_2(d[0])
        data[i].append(map_types[type])

    ranks = sorted(data, key=cmp_to_key(compare))
    result = 0
    for i, r in enumerate(ranks):
        result += (i+1)*r[1]

    print("Result 2: ", result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
