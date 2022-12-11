from aocd import lines


def find_code(keypad, start_pos, instrs):
    code = []
    pos = list(start_pos)

    for instr in instrs:
        for c in instr:
            if c == "U" and pos[0] > 0 and keypad[pos[0] - 1][pos[1]]:
                pos[0] -= 1
            elif c == "D" and pos[0] < len(keypad) - 1 and keypad[pos[0] + 1][pos[1]]:
                pos[0] += 1
            elif c == "L" and pos[1] > 0 and keypad[pos[0]][pos[1] - 1]:
                pos[1] -= 1
            elif c == "R" and pos[1] < len(keypad) - 1 and keypad[pos[0]][pos[1] + 1]:
                pos[1] += 1
        code.append(keypad[pos[0]][pos[1]])

    return "".join(code)


keypad1 = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]
p1 = find_code(keypad1, (1, 1), lines)


keypad2 = [
    [None, None, "1", None, None],
    [None, "2", "3", "4", None],
    ["5", "6", "7", "8", "9"],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None],
]
p2 = find_code(keypad2, (2, 2), lines)
