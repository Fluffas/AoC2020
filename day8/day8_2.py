import sys
from copy import deepcopy

with open(sys.argv[1], "r") as file:
    input = [line.strip().split() for line in file.readlines()]
    input = [[op, int(arg)] for op, arg in input]

    def run(program):
        accumulator = 0
        i = 0
        ran = set()
        while 0 <= i < len(program):
            if i in ran:
                return None
            ran.add(i)
            op = program[i][0]
            arg = program[i][1]
            if op == "acc":
                accumulator += arg
                i += 1
            elif op == "jmp":
                i += arg
            else:
                i += 1
        return accumulator

    for j in range(len(input)):
        tempinput = deepcopy(input)
        if tempinput[j][0] == "jmp":
            tempinput[j][0] = "nop"
        elif tempinput[j][0] == "nop":
            tempinput[j][0] = "jmp"
        else:
            continue
        x = run(tempinput)
        if x:
            print(x)
            sys.exit()
