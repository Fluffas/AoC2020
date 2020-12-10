import sys
with open(sys.argv[1], "r") as file:
    input = [int(i) for i in file.readlines()]
    input.append(0)
    input.sort()
    input.append(input[-1] + 3)

    temp = [1]
    for i in range(1, len(input)):
        cmb = 0
        for j in range(i-3, i):
            if input[j] + 3 >= input[i] and j >= 0:
                cmb += temp[j]
        temp.append(cmb)

    print(temp[-1])
