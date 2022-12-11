from aocd import lines


def exec_assembunny(instrs, a=0, b=0, c=0, d=0):
    pc = 0
    regs = {"a": a, "b": b, "c": c, "d": d}

    while pc < len(instrs):
        instr = instrs[pc]
        op = instr[0]
        if op == "cpy":
            if instr[1] in regs:
                regs[instr[2]] = regs[instr[1]]
            else:
                regs[instr[2]] = int(instr[1])
        elif op == "inc":
            regs[instr[1]] += 1
        elif op == "dec":
            regs[instr[1]] -= 1
        elif op == "jnz":
            if instr[1] in regs:
                val = regs[instr[1]]
            else:
                val = int(instr[1])
            if val != 0:
                pc += int(instr[2])
                continue
        pc += 1

    return regs


instrs = [line.split() for line in lines]

p1 = exec_assembunny(instrs)["a"]
p2 = exec_assembunny(instrs, c=1)["a"]
