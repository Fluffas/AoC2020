import sys

with open(sys.argv[1], "r") as file:
    input = [line.strip() for line in file.readlines()]
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    ans = 1
    for dx, dy in slopes:
        x = 0
        y = 0
        score = 0
        while y < len(input):
            if input[y][x] == "#":
                score += 1
            x += dx
            if x >= len(input[y]):
                x -= len(input[y])
            y += dy
        ans *= score
    print(ans)
