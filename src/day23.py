from aocd import lines


toggles = {
    "inc": "dec",
    "dec": "inc",
    "jnz": "cpy",
    "cpy": "jnz",
    "tgl": "inc",
}


def exec_assembunny(instrs, a=0, b=0, c=0, d=0):
    pc = 0
    regs = {"a": a, "b": b, "c": c, "d": d}

    while pc < len(instrs):
        instr = instrs[pc]
        op = instr[0]
        if op == "cpy":
            if instr[2] in regs:
                regs[instr[2]] = regs[instr[1]] if instr[1] in regs else int(instr[1])
        elif op == "add":
            if instr[2] in regs:
                regs[instr[2]] += regs[instr[1]] if instr[1] in regs else int(instr[1])
        elif op == "mul":
            if instr[2] in regs:
                regs[instr[2]] *= regs[instr[1]] if instr[1] in regs else int(instr[1])
        elif op == "inc":
            regs[instr[1]] += 1
        elif op == "dec":
            regs[instr[1]] -= 1
        elif op == "jnz":
            val = regs[instr[1]] if instr[1] in regs else int(instr[1])
            if val != 0:
                pc += regs[instr[2]] if instr[2] in regs else int(instr[2])
                continue
        elif op == "tgl":
            offset = regs[instr[1]]
            try:
                target = instrs[pc + offset]
                target[0] = toggles[target[0]]
            except IndexError:
                pass
        pc += 1

    return regs


instrs = [line.split() for line in lines]
p1 = exec_assembunny(instrs, a=7)["a"]

instrs = [line.split() for line in lines]
# Replace the double-nested multiplication loop with a new multiplication op. This could
# probably be made more general, but that sounds like a lot of work.
instrs[5:10] = [
    ["noop"],
    ["mul", "d", "c"],
    ["add", "c", "a"],
    ["cpy", "0", "d"],
    ["cpy", "0", "c"],
]
p2 = exec_assembunny(instrs, a=12)["a"]
