import sys
import re

valid = 0
with open(sys.argv[1], "r") as file:
    input = [line.strip() for line in file.readlines()]

    for x in input:
        split = x.split(": ")
        vals = list(map(int, re.findall(r"\d+", split[0])))
        letter = split[0][len(split[0])-1]
        pw = split[1]

        counter = 0
        for match in re.finditer(letter, pw):
            counter += 1

        if vals[0] <= counter <= vals[1]:
            valid += 1

print(valid)
