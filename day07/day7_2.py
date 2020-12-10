import sys

with open(sys.argv[1], "r") as file:
    input = [line.replace("bags", "").replace("bag", "").replace(".", "").strip() for line in file.readlines()]

    rules = {}
    for line in input:
        bag, contents = line.split("  contain ")
        if contents.startswith("no"):
            continue
        rules[bag] = [(int(content[0]), content.strip()[2:]) for content in contents.split(", ")]

    def countbags(c):
        count = 0
        if c in rules:
            for amount, color in rules[c]:
                count += amount
                count += amount * countbags(color)
        return count

    print(countbags("shiny gold"))
