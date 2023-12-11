#!/usr/bin/env python3


import re


def load_input():
    data = dict()
    seeds = None

    pattern = re.compile('(\w*)-to-(\w*) map:')
    with open('input') as fd:
        for i, line in enumerate(fd):
            line = line.strip()
            if i == 0:
                k, numbers = line.split(':')
                seeds = [int(j) for j in numbers.split()]
            elif not line:
                pass
            elif 'map' in line:
                match = pattern.search(line)
                key = match.group(1)
                k1 = match.group(2)
                data[key] = {'n': k1, 'ranges': list()}
            else:
                numbers = [int(j) for j in line.split()]
                data[key]['ranges'].append(tuple(numbers))
                data[key]['ranges'].sort(key=lambda x: x[1])

    # print(data)
    return seeds, data


def part1():
    seeds, data = load_input()
    locations = list()
    for seed in seeds:
        number = seed
        d = data['seed']
        for _ in range(len(data)):
            for v in d['ranges']:
                if v[1] <= number < v[1] + v[2]:
                    number += v[0] - v[1]
                    break
            if d['n'] == 'location':
                locations.append(number)
                break
            d = data[d['n']]

    result = min(locations)

    print("Result 1: ", result)


def get_ranges(data, t):
    ranges = list()
    stop = False
    for d in data:
        while True:
            t_e = t[0] + t[1] - 1
            d_e = d[1] + d[2] - 1
            t_s = t[0]
            d_s = d[1]
            if t_e < d_s:
                ranges.append(t)
                stop = True
                break
            elif t_s > d_e:
                break
            elif t_s < d_s:
                ranges.append((t_s, d_s-t_s+1))
                t = (d_s, t_e-d_s-1)
            elif t_e <= d_e:
                ranges.append((t_s-(d[1]-d[0]), t_e-t_s+1))
                stop = True
                break
            elif t_e > d_e:
                t = (d_e+1, t_e-d_e)
                ranges.append((t_s-(d[1]-d[0]), d_e-t_s+1))
            else:
                print("Error")
        if stop:
            break
    else:
        ranges.append(t)
    return ranges


def part2():
    seeds, data = load_input()
    mins = list()
    for i in range(len(seeds)//2):
        t = [(seeds[2*i], seeds[2*i+1])]
        d = data['seed']
        for _ in range(len(data)):
            temp = list()
            for a in t:
                temp.extend(get_ranges(d['ranges'], a))
            t = temp
            if d['n'] == 'location':
                mins.append(min([x[0] for x in t]))
                break
            d = data[d['n']]

    result = min(mins)
    print("Result 2: ", result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
