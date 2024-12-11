import math
from collections import defaultdict


def puzzle_1():
    stones = original_stones
    for idx in range(25):
        stones = blink(stones)
    print(sum(val for val in stones.values()))


def puzzle_2():
    stones = original_stones
    for idx in range(75):
        stones = blink(stones)
    print(sum(val for val in stones.values()))


def stone_size(stone):
    return int(math.log10(stone))+1


def blink(stones):
    new_stones = defaultdict(int)
    for stone, amount in stones.items():
        if stone == 0:
            new_stones[1] += amount
        elif stone_size(stone) % 2 == 0:
            new_len = int(stone_size(stone)/2)
            first = int(str(stone)[:new_len])
            second = int(str(stone)[new_len:])
            new_stones[first] += amount
            new_stones[second] += amount
        else:
            new_stones[stone * 2024] += amount
    return new_stones


if __name__ == '__main__':
    with open("input.txt") as file:
        original_stones = defaultdict(int)
        for stone in file.read().strip().split():
            original_stones[int(stone)] += 1
        puzzle_1()
        puzzle_2()