from aocd import submit, get_data


def main():
    day = 2
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""": 2,
    }
    test_data_b = {
"""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""": 1,
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
    for line in data.splitlines():
        count, letter, password = line.split()
        c0, c1 = count.split("-")
        letter = letter[:-1]
        if int(c0) <= password.count(letter) <= int(c1):
            res += 1
    return res


def solve_b(data):
    res = 0
    for line in data.splitlines():
        count, letter, password = line.split()
        c0, c1 = count.split("-")
        letter = letter[:-1]
        if sum((password[int(c0)-1] == letter,
                password[int(c1)-1] == letter)) == 1:
            res += 1
    return res


if __name__ == "__main__":
    main()
