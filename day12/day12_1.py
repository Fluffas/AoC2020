import sys
with open(sys.argv[1], "r") as file:
    foo = [line.strip() for line in file.readlines()]

    north = 0
    east = 1
    south = 2
    west = 3
    x = y = 0
    facing = east
    for instruction in foo:
        act = instruction[0]
        val = int(instruction[1:])
        if act == "N":
            y += val
        elif act == "S":
            y -= val
        elif act == "E":
            x += val
        elif act == "W":
            x -= val
        elif act == "L":
            facing = ((facing - val / 90) + 4) % 4
        elif act == "R":
            facing = (facing + val / 90) % 4
        elif act == "F":
            if facing == north:
                y += val
            elif facing == south:
                y -= val
            elif facing == east:
                x += val
            elif facing == west:
                x -= val

    print(abs(x) + abs(y))
