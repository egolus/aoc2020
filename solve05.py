from aocd import submit, get_data


def main():
    day = 5
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL""": 820,
    }
    test_data_b = {
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
    highest = 0
    for line in data.splitlines():
        startR, endR = 0, 127
        startC, endC = 0, 7
        for c in line:
            if c in ("B", "F"):
                mid = (endR-startR) // 2
                if c == "F":
                    endR = startR + mid
                else:
                    startR = startR + mid + 1
            elif c in ("L", "R"):
                mid = (endC-startC) // 2
                if c == "L":
                    endC = startC + mid
                else:
                    startC = startC + mid + 1
        sid = startR * 8 + startC
        highest = max((highest, sid))
    return highest


def solve_b(data):
    sids = set()
    for line in data.splitlines():
        startR, endR = 0, 127
        startC, endC = 0, 7
        for c in line:
            if c in ("B", "F"):
                mid = (endR-startR) // 2
                if c == "F":
                    endR = startR + mid
                else:
                    startR = startR + mid + 1
            elif c in ("L", "R"):
                mid = (endC-startC) // 2
                if c == "L":
                    endC = startC + mid
                else:
                    startC = startC + mid + 1
        sid = startR * 8 + startC
        sids.add(sid)
    for sid in range(min(sids), max(sids)):
        if sid not in sids:
            return sid


if __name__ == "__main__":
    main()
