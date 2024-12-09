import re


def puzzle_1(instructions):
    groups = re.findall("mul\((\d+),(\d+)\)", instructions)
    print(sum([int(x) * int(y) for x, y in groups]))


def puzzle_2(instructions):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"
    groups = re.findall(pattern, instructions)
    do = True
    sum = 0
    for group in groups:
        if group[3] == "don't()":
            do = False
        elif group[2] == "do()":
            do = True
        elif do:
            sum += int(group[0]) * int(group[1])
    print(sum)


if __name__ == '__main__':
    with open("input.txt") as file:
        instructions = file.read()
        puzzle_1(instructions)
        puzzle_2(instructions)
