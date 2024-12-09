def puzzle_1(l1, l2):
    print(sum([abs(int(x) - int(y)) for x, y in zip(l1, l2)]))


def puzzle_2(l1 ,l2):
    print(sum([int(x) * l2.count(x) for x in l1]))


if __name__ == '__main__':
    with open("input.txt") as file:
        split_lines = [line.split() for line in file.readlines()]
        l1, l2 = zip(*split_lines)
        puzzle_1(sorted(l1), sorted(l2))
        puzzle_2(l1, l2)
