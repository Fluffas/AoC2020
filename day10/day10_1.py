import sys
with open(sys.argv[1], "r") as file:
    input = [int(i) for i in file.readlines()]
    input.append(0)
    input.sort()
    input.append(input[-1] + 3)

    diff1 = 0
    diff3 = 0
    for i in range(1, len(input)):
        diff = input[i] - input[i-1]
        if diff == 1:
            diff1 += 1
        elif diff == 3:
            diff3 += 1

    print(diff1 * diff3)
