import sys
with open(sys.argv[1], "r") as file:
    input = [int(i) for i in file.readlines()]

    for x in input:
        for y in input:
            if x + y == 2020:
                print(x * y)
                sys.exit()
