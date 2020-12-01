import sys
input = sys.argv[1]

with open(input, "r") as x:
    for line1 in x:
        num1 = int(line1.strip())

        with open(input, "r") as y:
            for line2 in y:
                num2 = int(line2.strip())

                if num1 + num2 == 2020:
                    print(num1 * num2)
                    sys.exit()
