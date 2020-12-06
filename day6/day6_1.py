import sys

with open(sys.argv[1], "r") as file:
    input = [foo.replace("\n", "") for foo in file.read().split("\n\n")]

    ans = 0
    for group in input:
        ans += len(set(group))
    print(ans)
