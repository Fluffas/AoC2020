import sys
with open(sys.argv[1], "r") as file:
    input = file.readlines()

    for x in input:
        num1 = int(x.strip())

        for y in input:
            num2 = int(y.strip())

            for z in input:
                num3 = int(z.strip())

                if num1 + num2 + num3 == 2020:
                    print(num1 * num2 * num3)
                    sys.exit("Success")
