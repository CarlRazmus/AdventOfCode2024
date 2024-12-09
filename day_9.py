def puzzle_1():
    last_char_idx = len(s) - 1
    current_idx = 0
    compacted_s = ""
    while (current_idx <= last_char_idx):
        if (s[current_idx] != "."):
            compacted_s += s[current_idx]
        else:
            compacted_s += s[last_char_idx]
            last_char_idx = get_next_char_idx(last_char_idx)
        current_idx += 1

    tot = 0
    print(compacted_s)
    for idx, c in enumerate(compacted_s):
        if c != ".":
            tot += int(c) * idx
            print(str(idx) + " * " + c)
    print(tot)

def get_next_char_idx(curr_idx):
    next_idx = curr_idx - 1
    while(s[next_idx] == "."):
        next_idx -= 1
    return next_idx

def puzzle_2():
    pass


if __name__ == '__main__':
    with open("input.txt") as file:
        file_content = file.read().strip()
        s = ""
        block_id = 0
        for idx in range(len(file_content)):
            if idx % 2 == 0:
                s += str(block_id) * int(file_content[idx])
                block_id += 1
            else:
                s += "." * int(file_content[idx])
        print(s)

        puzzle_1()
        puzzle_2()
