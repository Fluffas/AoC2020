import sys
with open(sys.argv[1], "r") as file:
    foo = [line.strip() for line in file.readlines()]
    buses = foo[1].split(",")
    diffs = [(int(bus), diff) for diff, bus in enumerate(buses) if bus != "x"]

    i = diffs[0][0]
    ts = 0
    for bus, diff in diffs[1:]:
        while (ts + diff) % bus != 0:
            ts += i
        i *= bus
    print(ts)
