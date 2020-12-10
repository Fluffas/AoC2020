import sys

with open(sys.argv[1], "r") as file:
    input = file.read().split("\n\n")

    ans = 0
    for group in input:
        people = group.split()
        ans += len(list(set.intersection(*map(set, people))))
    print(ans)
