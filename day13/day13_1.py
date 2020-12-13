import sys
with open(sys.argv[1], "r") as file:
    foo = [line.strip() for line in file.readlines()]
    ts = int(foo[0])
    buses = [int(bus) for bus in foo[1].split(",") if bus != "x"]

    swait = ts
    for bus in buses:
        wait = abs(ts % bus - bus)
        if wait < swait:
            swait = wait
            ans = swait * bus
    print(ans)
