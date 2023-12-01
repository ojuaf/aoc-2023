#!/usr/bin/env python3


mapping = {'one': 1, 'two': 2, 'three': 3, 'four': 4,'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def load_input():
    with open('input') as fd:
        data = list()
        for line in fd:
            data.append(line.strip())

    return data


def get_integer_part1(line, it):
    for i in it:
        try:
            digit = int(line[i])
            break
        except:
            pass
    return digit


def get_integer_part2(line, it):
    digit = None
    for i in it:
        try:
            digit = int(line[i])
            break
        except:
            pass

        for k in mapping.keys():
            if line[i:].startswith(k):
                digit = mapping[k]
                break
        if digit is not None:
            break

    return digit


def main():
    data = load_input()

    numbers = list()
    for line in data:
        it = range(len(line))
        first = get_integer_part1(line, it)

        it = range(len(line), -1, -1)
        last = get_integer_part1(line, it)

        numbers.append(10*first + last)

    result = sum(numbers)
    print("Result 1: ", result)

    # Task 2
    numbers = list()
    for line in data:
        it = range(len(line))
        first = get_integer_part2(line, it)

        it = range(len(line), -1, -1)
        last = get_integer_part2(line, it)

        numbers.append(10*first + last)

    result = sum(numbers)
    print("Result 2: ", result)


if __name__ == '__main__':
    main()
