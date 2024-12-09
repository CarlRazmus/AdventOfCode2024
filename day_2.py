from itertools import pairwise
import operator


def ok_seq(report):
    op = operator.lt if report[0] - report[1] < 0 else operator.gt
    for x1, x2 in pairwise(report):
        if not (op(x1, x2) and abs(x1 - x2) <= 3):
            return 0
    return 1


def puzzle_1(reports):
    counts = 0
    for report in reports:
        counts += ok_seq(report)
    print(counts)


def puzzle_2(reports):
    counts = 0
    for report in reports:
        variants = list()
        variants.append(report)
        for idx, _ in enumerate(report):
            variants.append(report[:idx] + report[idx + 1:])
        counts += max([ok_seq(r) for r in variants])
    print(counts)


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [[int(x) for x in line.split()] for line in file.readlines()]
        puzzle_1(lines)
        puzzle_2(lines)
