import sys

with open(sys.argv[1], "r") as file:
    input = [line.strip().split() for line in file.readlines()]
    input = [[op, int(arg)] for op, arg in input]

    accumulator = 0
    i = 0
    ran = set()
    while 0 <= i < len(input):
        if i in ran:
            print(accumulator)
            sys.exit()
        ran.add(i)
        op = input[i][0]
        arg = input[i][1]
        if op == "acc":
            accumulator += arg
            i += 1
        elif op == "jmp":
            i += arg
        else:
            i += 1
