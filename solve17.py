from aocd import submit, get_data


def main():
    day = 17
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
""".#.
..#
###""": 112,
    }
    test_data_b = {
# """.#.
# ..#
# ###""": 112,
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


def solve_a(data):
    active = set()

    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                active.add((0, y, x))

    for step in range(6):
        minx = min(x for z, y, x in active)
        miny = min(y for z, y, x in active)
        minz = min(z for z, y, x in active)
        maxx = max(x for z, y, x in active)
        maxy = max(y for z, y, x in active)
        maxz = max(z for z, y, x in active)

        newactive = set()
        for z in range(minz-1, maxz+2):
            for y in range(miny-1, maxy+2):
                for x in range(minx-1, maxx+2):
                    neighbours = set()
                    for zi in range(-1, 2):
                        for yi in range(-1, 2):
                            for xi in range(-1, 2):
                                if (
                                    (z+zi, y+yi, x+xi) in active and
                                    (z+zi, y+yi, x+xi) != (z, y, x)
                                ):
                                    neighbours.add((z+zi, y+yi, x+xi))
                    if (z, y, x) in active and 2 <= len(neighbours) <= 3:
                        newactive.add((z, y, x))
                    elif (z, y, x) not in active and len(neighbours) == 3:
                        newactive.add((z, y, x))
        active = newactive
    return len(active)


def solve_b(data):
    active = set()

    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                active.add((0, 0, y, x))

    for step in range(6):
        minx = min(x for w, z, y, x in active)
        miny = min(y for w, z, y, x in active)
        minz = min(z for w, z, y, x in active)
        minw = min(w for w, z, y, x in active)
        maxx = max(x for w, z, y, x in active)
        maxy = max(y for w, z, y, x in active)
        maxz = max(z for w, z, y, x in active)
        maxw = max(w for w, z, y, x in active)

        newactive = set()
        for w in range(minw-1, maxw+2):
            for z in range(minz-1, maxz+2):
                for y in range(miny-1, maxy+2):
                    for x in range(minx-1, maxx+2):
                        neighbours = set()
                        for wi in range(-1, 2):
                            for zi in range(-1, 2):
                                for yi in range(-1, 2):
                                    for xi in range(-1, 2):
                                        if (
                                            (w+wi, z+zi, y+yi, x+xi) in active and
                                            (w+wi, z+zi, y+yi, x+xi) != (w, z, y, x)
                                        ):
                                            neighbours.add((w+wi, z+zi, y+yi, x+xi))
                        if (w, z, y, x) in active and 2 <= len(neighbours) <= 3:
                            newactive.add((w, z, y, x))
                        elif (w, z, y, x) not in active and len(neighbours) == 3:
                            newactive.add((w, z, y, x))
        active = newactive
    return len(active)


if __name__ == "__main__":
    main()
