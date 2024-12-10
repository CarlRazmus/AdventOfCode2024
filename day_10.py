def puzzle_1():
    tot = 0
    for pos in start_positions:
        print("startpos", pos)
        n = get_hikable_roads(pos, [], 0)
        print(n)
        tot += n
    print("sum", tot)

def get_hikable_roads(pos, visited_pos, tot):
    new_visited_pos = visited_pos + [pos]
    if heights[pos] == 9:
        return tot + 1
    neighbours = get_hikable_neighbours(pos, new_visited_pos)
    if len(neighbours) == 0:
        return tot
    for neighbour in neighbours:
        tot = get_hikable_roads(neighbour, new_visited_pos, tot)
    return tot


def puzzle_2():
    pass


def get_hikable_neighbours(pos, visited_pos):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    curr_height = heights[pos]
    hikable_neighbours = list()
    for dir in dirs:
        neighbour_pos = tuple(map(lambda i, j: i + j, pos, dir))
        if neighbour_pos in visited_pos:
            continue
        if neighbour_pos[1] in range(HEIGHT) and neighbour_pos[0] in range(WIDTH):
            if heights[neighbour_pos] - curr_height == 1:
                hikable_neighbours.append(neighbour_pos)
    return hikable_neighbours



if __name__ == '__main__':

    with open("input.txt") as file:
        start_positions = list()
        heights = dict()
        lines = file.readlines()
        HEIGHT = len(lines)
        WIDTH = len(lines[0].strip())
        for y, line in enumerate(lines):
            for x, val in enumerate(line.strip()):
                if val == "0":
                    start_positions.append((int(x), int(y)))
                heights[(int(x), int(y))] = int(val)

        puzzle_1()
        puzzle_2()
