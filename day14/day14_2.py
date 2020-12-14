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

            temp = []
            for maskbit, bit in zip(mask, format(addr, "036b")):
                if maskbit == "0":
                    temp.append(bit)
                else:
                    temp.append(maskbit)
            maskaddr = "".join(temp)

            addresses = [maskaddr]
            for i in range(maskaddr.count("X")):
                new = []
                for a in addresses:
                    new.append(a.replace("X", "1", 1))
                    new.append(a.replace("X", "0", 1))
                addresses = new

            for a in addresses:
                mem[int(a, 2)] = val

    print(sum(mem.values()))
