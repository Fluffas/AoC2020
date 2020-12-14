import sys
with open(sys.argv[1], "r") as file:
    foo = [line.strip().split(" = ") for line in file.readlines()]

    mem = {}
    for cmd, arg in foo:
        if cmd[:4] == "mask":
            mask = arg
        elif cmd[:3] == "mem":
            addr = int(cmd[4:-1])
            val = int(arg)
            val &= int(mask.replace("X", "1"), 2)
            val |= int(mask.replace("X", "0"), 2)
            mem[addr] = val
    print(sum(mem.values()))
