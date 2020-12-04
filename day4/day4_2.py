import sys
import string

with open(sys.argv[1], "r") as file:
    input = [foo.replace("\n", " ") for foo in file.read().split("\n\n")]

    fields = {
        "byr": lambda x: 1920 <= int(x) <= 2002,
        "iyr": lambda x: 2010 <= int(x) <= 2020,
        "eyr": lambda x: 2020 <= int(x) <= 2030,
        "hgt": lambda x: (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76),
        "hcl": lambda x: len(x) == 7 and x[0] == "#" and all(y in string.hexdigits for y in x[1:]),
        "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": lambda x: len(x) == 9 and x.isdecimal()
    }
    valid = 0

    for item in input:
        passport = {}
        for thing in item.split(" "):
            field, val = thing.split(":")
            passport[field] = val

        if all(key in passport.keys() for key in fields):
            if all(fields[key](passport[key]) for key in fields):
                valid += 1

    print(valid)
