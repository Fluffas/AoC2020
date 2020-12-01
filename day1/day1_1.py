import sys
with open(sys.argv[1], "r") as file:
    input = file.readlines()

    for x in input:
        num1 = int(x.strip())

        for y in input:
            num2 = int(y.strip())

            if num1 + num2 == 2020:
                print(num1 * num2)
                sys.exit("Success")
