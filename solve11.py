from aocd import submit, get_data


def main():
    day = 11
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""": 37,
    }
    test_data_b = {
"""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""": 26,
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_a = solve_a(data)
    print(f"result a: {result_a}\n")
    submit(result_a, part="a", day=day, year=year)

    for i, (test, true) in enumerate(test_data_b.items()):
        result = solve_b(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_b = solve_b(data)
    print(f"result b: {result_b}\n")
    submit(result_b, part="b", day=day, year=year)


def printGrid(empty, full, maxy, maxx):
    for y in range(maxy+1):
        for x in range(maxx+1):
            if (y, x) in empty:
                print("L", end="")
            elif (y, x) in full:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()


def solve_a(data):
    full = set()
    empty = set()

    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            if c == "L":
                empty.add((y, x))
            elif c == "#":
                full.add((y, x))

    maxx = max(x for y, x in empty)
    maxy = max(y for y, x in empty)

    while True:
        newFull = set()
        newEmpty = set()
        for y in range(maxy+1):
            for x in range(maxx+1):
                if (not (y, x) in full) and (not (y, x) in empty):
                    continue
                adjacent = (
                    (y-1, x-1),
                    (y-1, x),
                    (y-1, x+1),
                    (y, x-1),
                    (y, x+1),
                    (y+1, x-1),
                    (y+1, x),
                    (y+1, x+1),
                )
                if not any(a in full for a in adjacent):
                    newFull.add((y, x))
                elif (y, x) in full and sum([a in full for a in adjacent]) >= 4:
                    newEmpty.add((y, x))
                else:
                    if (y, x) in full:
                        newFull.add((y, x))
                    else:
                        newEmpty.add((y, x))

        if full == newFull:
            break
        full = newFull
        empty = newEmpty

    return len(full)


def solve_b(data):
    full = set()
    empty = set()

    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            if c == "L":
                empty.add((y, x))
            elif c == "#":
                full.add((y, x))

    maxx = max(x for y, x in empty)
    maxy = max(y for y, x in empty)
    printGrid(empty, full, maxy, maxx)

    moves = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    )
    while True:
        newFull = set()
        newEmpty = set()
        for y in range(maxy+1):
            for x in range(maxx+1):
                adjacent = set()
                for move in moves:
                    ay = y + move[0]
                    ax = x + move[1]
                    while (ay, ax) not in full and (ay, ax) not in empty:
                        if ay > maxy or ay < 0 or ax > maxx or ax < 0:
                            break
                        ay += move[0]
                        ax += move[1]
                    adjacent.add((ay, ax))

                if (not (y, x) in full) and (not (y, x) in empty):
                    continue
                if not any(a in full for a in adjacent):
                    newFull.add((y, x))
                elif (y, x) in full and sum([a in full for a in adjacent]) >= 5:
                    newEmpty.add((y, x))
                else:
                    if (y, x) in full:
                        newFull.add((y, x))
                    else:
                        newEmpty.add((y, x))
        printGrid(empty, full, maxy, maxx)

        if full == newFull:
            break
        full = newFull
        empty = newEmpty

    return len(full)


if __name__ == "__main__":
    main()
