from collections import defaultdict
from itertools import combinations


# def get_combinations(l):
#    combos = list()
#    for x, val1 in enumerate(l):
#        for val2 in l[:x] + l[x+1:]:
#            combos.append((val1, val2))
#    return combos

def tuple_add(t1, t2):
    return tuple(map(lambda i, j: i + j, t1, t2))


def tuple_subtract(t1, t2):
    return tuple(map(lambda i, j: i - j, t1, t2))


def get_antinodes(p1, p2):
    dir = tuple_subtract(p1, p2)
    an1 = tuple_add(p1, dir)
    an2 = tuple_subtract(p2, dir)
    return [v for v in [an1, an2] if v[1] in range(HEIGHT) and v[0] in range(WIDTH)]


def is_inside_map(p):
    return p[1] in range(HEIGHT) and p[0] in range(WIDTH)


def get_resonant_antinodes(p1, p2):
    l = list()
    dir = tuple_subtract(p1, p2)
    p1 = tuple_add(p1, dir)
    p2 = tuple_subtract(p2, dir)

    while is_inside_map(p1) or is_inside_map(p2):
        if is_inside_map(p1):
            l.append(p1)
            p1 = tuple_add(p1, dir)
        if is_inside_map(p2):
            l.append(p2)
            p2 = tuple_subtract(p2, dir)
    return l


def puzzle_1():
    anti_nodes = set()
    for node, positions in nodes.items():
        combos = list(combinations(positions, 2))
        for p1, p2 in combos:
            for node in get_antinodes(p1, p2):
                anti_nodes.add(node)
        # anti_nodes = [get_antinodes(p1, p2) for p1, p2 in combos]
    print(len(anti_nodes))


def puzzle_2():
    anti_nodes = set()
    for node, positions in nodes.items():
        combos = list(combinations(positions, 2))
        for p1, p2 in combos:
            for node in get_resonant_antinodes(p1, p2):
                anti_nodes.add(node)
        # anti_nodes = [get_antinodes(p1, p2) for p1, p2 in combos]

    print_puzzle(anti_nodes)
    print("before nodes: ", len(anti_nodes))
    for char, positions in nodes.items():
        if len(positions) > 1:
            for pos in positions:
                anti_nodes.add(pos)
    print("after nodes: ", len(anti_nodes))
    #print(sum([len(v) for v in nodes.values()]))


def print_puzzle(anti_nodes):
    for y, line in enumerate(lines):
        output = ""
        for x, char in enumerate(line):
            if (x, y) in anti_nodes:
                output += "#"
            else:
                output += char
        print(output)




if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [[c for c in line.strip()] for line in file.readlines()]
        nodes = defaultdict(list)
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char != ".":
                    nodes[char].append((x, y))
        HEIGHT = len(lines)
        WIDTH = len(lines[0])
        print(nodes)
        puzzle_1()
        puzzle_2()
