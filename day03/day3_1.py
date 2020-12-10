import sys

with open(sys.argv[1], "r") as file:
    input = [line.strip() for line in file.readlines()]

    x = 0
    score = 0
    for y in input:
        if y[x] == "#":
            score += 1
        x += 3
        if x >= len(y):
            x -= len(y)
    print(score)
