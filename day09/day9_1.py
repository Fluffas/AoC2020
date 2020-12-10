import sys
with open(sys.argv[1], "r") as file:
    input = [int(i) for i in file.readlines()]

    def findSum(list, sum):
        for i in list:
            for j in list:
                if i + j == sum:
                    return True
        return False

    for i in range(25, len(input)):
        num = input[i]
        preamble = input[i-25:i]
        x = findSum(preamble, num)
        if not x:
            print(num)
            sys.exit()

