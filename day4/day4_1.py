import sys

with open(sys.argv[1], "r") as file:
    input = [foo.replace("\n", " ") for foo in file.read().split("\n\n")]

    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = 0

    for item in input:
        passport = {}
        for thing in item.split(" "):
            field, val = thing.split(":")
            passport[field] = val

        if all(key in passport.keys() for key in fields):
            valid += 1

    print(valid)
