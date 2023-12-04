#!/usr/bin/env python3


def load_input():
    winning_numbers = list()
    draw_numbers = list()
    with open('input') as fd:
        for line in fd:
            line = line.strip()
            _, numbers = line.split(':')
            winning, draw = numbers.strip().split('|')
            winning = [int(i) for i in winning.strip().split()]
            draw = [int(i) for i in draw.strip().split()]
            winning_numbers.append(set(winning))
            draw_numbers.append(set(draw))
    return winning_numbers, draw_numbers


def part1():
    winning, draw = load_input()
    winners = list()
    for w, d in zip(winning, draw):
        winners.append(w.intersection(d))

    result = 0
    for w in winners:
        if len(w) > 0:
            result += 2**(len(w)-1)

    print("Result 1: ", result)


def part2():
    winning, draw = load_input()
    winners = list()
    for w, d in zip(winning, draw):
        winners.append(w.intersection(d))

    result = 0
    for w in winners:
        if len(w) > 0:
            result += 2**(len(w)-1)

    winners_len = [len(w) for w in winners]
    numbers = [1 for _ in range(len(winners_len))]
    for i in range(len(winners_len)):
        for j in range(i+1, i+1+winners_len[i]):
            numbers[j] += numbers[i]

    result = sum(numbers)
    print("Result 2: ", result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
