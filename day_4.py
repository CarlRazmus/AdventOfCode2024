def puzzle_1(lines):
    tot = 0
    for y in range(HEIGHT):
        for x in range(WIDTH):
            tot += verify_xmas(lines, (x, y))
    print(tot)


def verify_xmas(lines, pos):
    dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    return sum([is_xmas(lines, pos, dir) for dir in dirs])


def is_xmas(lines, pos, dir):
    for s in "XMAS":
        if (not pos[0] in range(WIDTH)) or (not pos[1] in range(HEIGHT)):
            return 0
        if lines[pos[1]][pos[0]] != s:
            return 0
        pos = tuple(map(lambda i, j: i + j, pos, dir))
    return 1


def verify_x_mas(lines):
    positions = [(x, y) for x in range(WIDTH) for y in range(HEIGHT)]
    return sum([is_x_mas(lines, (x, y)) for (x, y) in positions])


def puzzle_2(lines):
    tot = 0
    for _ in range(4):
        tot += verify_x_mas(lines)
        lines = list(reversed(list(zip(*lines))))
    print(tot)


def is_x_mas(lines, pos):
    if (not pos[0] in range(WIDTH - 2)) or (not pos[1] in range(HEIGHT - 2)):
        return 0

    x = pos[0]
    y = pos[1]
    m1 = lines[y][x] == "M"
    m2 = lines[y + 2][x] == "M"
    a1 = lines[y + 1][x + 1] == "A"
    s1 = lines[y][x + 2] == "S"
    s2 = lines[y + 2][x + 2] == "S"

    return 1 if m1 and m2 and a1 and s1 and s2 else 0


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [[s for s in line.strip()] for line in file.readlines()]
        HEIGHT = len(lines)
        WIDTH = len(lines[0])
        puzzle_1(lines)
        puzzle_2(lines)
