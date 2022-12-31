from aocd import submit, get_data
from rich import print as pprint


def main():
    day = 3
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""": 7,
    }
    test_data_b = {
"""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""": 336,
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
    res = 0
    grid = {}
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                grid[(y, x)] = c

    maxx = max(x for y, x in grid)
    maxy = max(y for y, x in grid)

    y, x = 0, 0
    while y < maxy+1:
        y += 1
        x = (x + 3) % (maxx + 1)
        if (y, x) in grid:
            res += 1
        else:
            grid[(y, x)] = "0"
    return res


def solve_b(data):
    res = 1
    grid = {}
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                grid[(y, x)] = c

    maxx = max(x for y, x in grid)
    maxy = max(y for y, x in grid)

    for dy, dx in ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1)):
        y, x = 0, 0
        r = 0
        while y < maxy+1:
            y += dy
            x = (x + dx) % (maxx + 1)
            print(y, x, x, (y, x) in grid)
            if (y, x) in grid:
                r += 1
        res *= r
    return res


if __name__ == "__main__":
    main()
