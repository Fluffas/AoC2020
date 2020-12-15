import sys
from collections import defaultdict
with open(sys.argv[1], "r") as file:
    start = list(map(int, file.readline().split(",")))

    # defaultdict fixes problem of appending undefined lists in dict
    spoken = defaultdict(list)
    numbers = []
    for i, num in enumerate(start, 1):
        spoken[num].append(i)
        numbers.append(num)

    for i in range(len(start) + 1, 30000000 + 1):
        prev = spoken[numbers[-1]]
        if len(prev) > 1:
            numbers.append(prev[-1] - prev[-2])
        else:
            numbers.append(0)
        spoken[numbers[-1]].append(i)

    print(numbers[-1])
