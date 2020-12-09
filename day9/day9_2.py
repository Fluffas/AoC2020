import sys
with open(sys.argv[1], "r") as file:
    input = [int(i) for i in file.readlines()]

    def findSum(array, sum):
        for i in array:
            for j in array:
                if i + j == sum:
                    return True
        return False

    def findSet(array, num):
        for j in range(len(array)):
            ans = 0
            y = 0
            numbers = set()
            while ans < num:
                ans += array[j+y]
                numbers.add(array[j+y])
                y += 1
            if ans == num:
                return numbers
        return None

    for i in range(25, len(input)):
        num = input[i]
        preamble = input[i-25:i]
        x = findSum(preamble, num)
        if not x:
            answer = list(sorted(findSet(input, num)))
            print(answer[0] + answer[-1])
            sys.exit()
