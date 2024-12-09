from collections import defaultdict
from functools import cmp_to_key
from time import perf_counter

def puzzle_1():
    valid_updates = [update for update in updates if is_order_ok(update)]
    print(sum([int(get_middle_val(l)) for l in valid_updates]))


def is_order_ok(update):
    for idx, page in enumerate(update):
        rules_after = rules[page]
        pages_before = update[:idx]
        if len(rules_after.intersection(pages_before)) > 0:
            return False
    return True


def puzzle_2():
    invalid_updates = [update for update in updates if not is_order_ok(update)]
    valid_updates = [sorted(u, key=cmp_to_key(compare)) for u in invalid_updates]
    print(sum([int(get_middle_val(update)) for update in valid_updates]))


def compare(a, b):
    if b in rules[a]:
        return 1
    elif a in rules[b]:
        return -1
    else:
        return 0


def set_rules():
    for rule in rules_input.split():
        first, last = rule.strip().split("|")
        rules[first].add(last)


def get_middle_val(l):
    middle_idx = int(len(l) / 2)
    return l[middle_idx]


if __name__ == '__main__':
    with open("input.txt") as file:
        rules_input, updates = file.read().split("\n\n")
        rules = defaultdict(set)
        set_rules()
        updates = [update.split(",") for update in updates.split()]
        puzzle_1()
        puzzle_2()
