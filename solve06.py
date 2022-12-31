from aocd import submit, get_data


def main():
    day = 6
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""abc

a
b
c

ab
ac

a
a
a
a

b""": 11,
    }
    test_data_b = {
"""abc

a
b
c

ab
ac

a
a
a
a

b""": 6,
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
    for group in data.split("\n\n"):
        ans = set()
        for c in group:
            if c != "\n":
                ans.add(c)
        res += len(ans)
    return res


def solve_b(data):
    res = 0
    for group in data.split("\n\n"):
        ans = {}
        for c in group:
            if c != "\n":
                if c in ans:
                    ans[c] += 1
                else:
                    ans[c] = 1
        for v in ans.values():
            if v == len(group.splitlines()):
                res += 1
    return res


if __name__ == "__main__":
    main()
