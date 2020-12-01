import sys
input = sys.argv[1]

with open(input, "r") as x:
    for line1 in x:
        num1 = int(line1.strip())

        with open(input, "r") as y:
            for line2 in y:
                num2 = int(line2.strip())

                with open(input, "r") as z:
                    for line3 in z:
                        num3 = int(line3.strip())

                        if num1 + num2 + num3 == 2020:
                            print(num1 * num2 * num3)
                            sys.exit()
