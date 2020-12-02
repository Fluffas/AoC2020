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

        if (pw[vals[0]-1] == letter and pw[vals[1]-1] != letter) or (pw[vals[0]-1] != letter and pw[vals[1]-1] == letter):
            valid += 1

print(valid)
