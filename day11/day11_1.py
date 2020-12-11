import sys
from copy import deepcopy
with open(sys.argv[1], "r") as file:
    foo = [list(line.strip()) for line in file.readlines()]

    def findadj(grid, y, x):
        adj = 0
        for j in [-1, 0, 1]:
            for i in [-1, 0, 1]:
                if not j == i == 0:
                    dy = y + j
                    dx = x + i
                    if 0 <= dy < len(grid) and 0 <= dx < len(grid[y]):
                        if grid[dy][dx] == "#":
                            adj += 1
        return adj

    newfoo = deepcopy(foo)
    changed = True
    while changed:
        changed = False
        for y in range(len(foo)):
            for x in range(len(foo[y])):
                if foo[y][x] == "L":
                    if findadj(foo, y, x) == 0:
                        newfoo[y][x] = "#"
                        changed = True
                elif foo[y][x] == "#":
                    if findadj(foo, y, x) >= 4:
                        newfoo[y][x] = "L"
                        changed = True
        foo = deepcopy(newfoo)

    print(sum([i == "#" for line in newfoo for i in line]))
