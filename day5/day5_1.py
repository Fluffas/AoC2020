import sys

with open(sys.argv[1], "r") as file:
    input = [line.strip() for line in file.readlines()]

    ans = 0

    for line in input:
        row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
        seat = int(line[7:].replace("L", "0").replace("R", "1"), 2)
        id = row * 8 + seat
        if id > ans:
            ans = id

    print(ans)
