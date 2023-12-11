
#!/usr/bin/env python3

import math as m

import networkx as nx


def load_input():
    data = list()
    with open('input') as fd:
        for line in fd:
            data.append(line.strip())

    return data


def get_neighbors(symbol, y, x):
    neighbors = []
    if symbol == '.':
        pass
    elif symbol == '|':
        neighbors = [(y-1, x), (y+1, x)]
    elif symbol == '-':
        neighbors = [(y, x+1), (y, x-1)]
    elif symbol == 'L':
        neighbors = [(y-1, x), (y, x+1)]
    elif symbol == 'J':
        neighbors = [(y-1, x), (y, x-1)]
    elif symbol == '7':
        neighbors = [(y+1, x), (y, x-1)]
    elif symbol == 'F':
        neighbors = [(y+1, x), (y, x+1)]
    elif symbol == 'S':
        neighbors = [(y+i, x+j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
        neighbors.remove((y, x))
    else:
        print("Error")
    return neighbors


def create_graph(data):
    graph = nx.Graph()
    start = None

    for y, d in enumerate(data):
        for x, symbol in enumerate(d):
            pos = (y, x)
            neighbors = get_neighbors(symbol, y, x)
            if symbol == 'S':
                start = pos
            if neighbors:
                for neighbor in neighbors:
                    n_y, n_x = neighbor
                    if 0 <= n_y < len(data) and 0 <= n_x < len(d):
                        check = get_neighbors(data[n_y][n_x], n_y, n_x)
                        if pos in check:
                            graph.add_edge(pos, neighbor)

    return graph, start


def get_region(graph, start):
    """"""
    margins = [start]
    inside = set()
    while True:
        next_margins = list()
        for pos in margins:
            y, x = pos
            neighbors = [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]
            for neighbor in neighbors:
                if neighbor not in graph.nodes() and neighbor not in inside:
                    next_margins.append(neighbor)
        inside.update(set(margins))
        margins = next_margins
        # print(inside)
        if not margins:
            break
    return inside


def part1():
    data = load_input()
    graph, start = create_graph(data)
    bfs_tree = nx.bfs_tree(graph, start)
    leaves = [node for node in bfs_tree.nodes() if bfs_tree.out_degree(node) == 0]
    mins = []
    # print(list(bfs_tree.edges()))
    for leaf in leaves:
        short = nx.shortest_path_length(graph, start, leaf)
        mins.append(short)

    result = max(mins)

    print("Result 1: ", result)


def part2():
    data = load_input()
    graph, start = create_graph(data)
    node = start
    prev_node = None
    inside = set()
    bfs_tree = nx.bfs_tree(graph, start)
    while True:
        neighbors = list(graph.neighbors(node))
        if prev_node is None:
            prev_node = neighbors[1]
        for neighbor in neighbors:
            if prev_node != neighbor:
                prev_node = node
                node = neighbor
                dir0 = tuple([i-j for i, j in zip(node, prev_node)])
                for neighbor in graph.neighbors(node):
                    if prev_node != neighbor:
                        dir1 = tuple([i-j for i, j in zip(neighbor, node)])

                left0 = (-dir0[1], dir0[0])
                left1 = (-dir1[1], dir1[0])
                lefts = [left0, left1]
                break
        for left in lefts:
            pos = tuple([i+j for i, j in zip(node, left)])
            if pos not in bfs_tree.nodes() and pos not in inside:
                inside.update(get_region(bfs_tree, pos))
        if node == start:
            break

    result = len(inside)
    print("Result 2: ", result)


def main():
    # part1()
    part2()


if __name__ == '__main__':
    main()
