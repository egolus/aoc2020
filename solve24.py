from aocd import submit, get_data


def main():
    day = 24
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""": 10,
    }
    test_data_b = {
"""sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""": 2208,
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


def move(coords, step) -> tuple:
    if step == "ne":
        coords = (coords[0] + 1, coords[1] - 1)
    elif step == "nw":
        coords = (coords[0], coords[1] - 1)
    elif step == "se":
        coords = (coords[0], coords[1] + 1)
    elif step == "sw":
        coords = (coords[0] - 1, coords[1] + 1)
    elif step == "w":
        coords = (coords[0] - 1, coords[1])
    elif step == "e":
        coords = (coords[0] + 1, coords[1])
    return coords


def adjacent(coords) -> list[tuple]:
    return [
        (coords[0], coords[1] - 1),
        (coords[0] + 1, coords[1] - 1),
        (coords[0] + 1, coords[1]),
        (coords[0], coords[1] + 1),
        (coords[0] - 1, coords[1] + 1),
        (coords[0] - 1, coords[1]),
    ]


def solve_a(data):
    black = set()
    for line in data.splitlines():
        m = ""
        pos = (0, 0)
        line = list(line)
        while line:
            while m not in ["ne", "nw", "se", "sw", "w", "e"]:
                m += line.pop(0)
            pos = move(pos, m)
            m = ""
        if pos in black:
            black.remove(pos)
        else:
            black.add(pos)
    return len(black)


def solve_b(data):
    black = set()
    for line in data.splitlines():
        m = ""
        pos = (0, 0)
        line = list(line)
        while line:
            while m not in ["ne", "nw", "se", "sw", "w", "e"]:
                m += line.pop(0)
            pos = move(pos, m)
            m = ""
        if pos in black:
            black.remove(pos)
        else:
            black.add(pos)
    for i in range(100):
        newBlack = set()
        maxQ = max(q for q, r in black)
        minQ = min(q for q, r in black)
        maxR = max(r for q, r in black)
        minR = min(r for q, r in black)
        for q in range(minQ - 1, maxQ + 2):
            for r in range(minR - 1, maxR + 2):
                neighbours = sum([neighbour in black for neighbour in adjacent((q, r))])
                if (q, r) in black and (1 <= neighbours <= 2):
                    newBlack.add((q, r))
                elif (q, r) not in black and neighbours == 2:
                    newBlack.add((q, r))
        black = newBlack
        print(f"{i} - {len(black)}")
    return len(black)

if __name__ == "__main__":
    main()
