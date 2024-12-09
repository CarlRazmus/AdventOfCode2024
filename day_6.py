
def puzzle_1():
    dir = start_dir
    pos = start_pos
    visited_pos = set()
    visited_pos.add(pos)

    while pos[0] in range(WIDTH) and pos[1] in range(HEIGHT):
        next_pos = tuple(map(lambda i, j: i + j, pos, dir))

        while next_pos in obstructions:
            next_pos


def get_next_dir(dir):
    idx = dirs.index(dir)
    return dirs[idx + 1 % 4]

def puzzle_2():
    pass

if __name__ == '__main__':

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    with open("input.txt") as file:
        obstructions = list()
        start_pos = (0, 0)
        start_dir = (0, -1)
        lines = file.readlines()
        HEIGHT = len(lines)
        WIDTH = len(lines[0])
        for y, line in enumerate(lines):
            for x, val in enumerate(line.strip()):
                if val == "^":
                    start_pos = (x, y)
                elif val == "#":
                    obstructions.append((x,y))
        puzzle_1()
        puzzle_2()