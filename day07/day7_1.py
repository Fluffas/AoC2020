import sys

with open(sys.argv[1], "r") as file:
    input = [line.replace("bags", "").replace("bag", "").replace(".", "").strip() for line in file.readlines()]

    rules = {}
    for line in input:
        bag, contents = line.split("  contain ")
        if contents.startswith("no"):
            continue
        rules[bag] = [(int(content[0]), content.strip()[2:]) for content in contents.split(", ")]

    count = 0
    prev = 1
    containssg = set()
    while count != prev:
        prev = count
        for rule in rules:
            if rule in containssg:
                continue
            for _, color in rules[rule]:
                if color in containssg or color == "shiny gold":
                    containssg.add(rule)
                count = len(containssg)

    print(count)
