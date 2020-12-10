import sys
import re

valid = 0
with open(sys.argv[1], "r") as file:
    input = [line.strip() for line in file.readlines()]

    for x in input:
        params, pw = x.split(": ")
        low, high = map(int, re.findall(r"\d+", params))
        letter = params[len(params)-1]

        if (pw[low-1] == letter and pw[high-1] != letter) or (pw[low-1] != letter and pw[high-1] == letter):
            valid += 1

print(valid)
