import sys
with open(sys.argv[1], "r") as file:
    foo = [line.strip() for line in file.readlines()]

    x = y = 0
    wx = 10
    wy = 1
    for instruction in foo:
        act = instruction[0]
        val = int(instruction[1:])
        if act == "N":
            wy += val
        elif act == "S":
            wy -= val
        elif act == "E":
            wx += val
        elif act == "W":
            wx -= val
        elif act == "L":
            rot = int(val / 90)
            for i in range(rot):
                wy, wx = wx, -wy
        elif act == "R":
            rot = int(val / 90)
            for i in range(rot):
                wy, wx = -wx, wy
        elif act == "F":
            y += val * wy
            x += val * wx

    print(abs(x) + abs(y))
