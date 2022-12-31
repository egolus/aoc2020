from aocd import submit, get_data


def main():
    day = 1
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""1721
979
366
299
675
1456""": 514579,
    }

    test_data_b = {
"""1721
979
366
299
675
1456""": 241861950,
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
    lines = data.splitlines()
    for i, line in enumerate(lines):
        for other in lines[i+1:]:
            print(line, other)
            if int(line) + int(other) == 2020:
                return int(line) * int(other)


def solve_b(data):
    lines = data.splitlines()
    for i, l0 in enumerate(lines):
        for j, l1 in enumerate(lines[i+1:]):
            for l2 in lines[j+1:]:
                if sum((int(l0), int(l1), int(l2))) == 2020:
                    return int(l0) * int(l1) * int(l2)


if __name__ == "__main__":
    main()
