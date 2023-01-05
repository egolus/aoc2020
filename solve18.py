from aocd import submit, get_data


def main():
    day = 18
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
        "1 + 2 * 3 + 4 * 5 + 6": 71,
        "1 + (2 * 3) + (4 * (5 + 6))": 51,
        "2 * 3 + (4 * 5)": 26,
        "5 + (8 * 3 + 9 + 3 * 4 * 3)": 437,
        "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))": 12240,
        "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2": 13632,
    }
    test_data_b = {
        "1 + 2 * 3 + 4 * 5 + 6": 231,
        "1 + (2 * 3) + (4 * (5 + 6))": 51,
        "2 * 3 + (4 * 5)": 46,
        "5 + (8 * 3 + 9 + 3 * 4 * 3)": 1445,
        "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))": 669060,
        "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2": 23340,
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
        waiting = []
        parens = []
        for c in line.split():
            if c.startswith("("):
                noParens = len([x for x in c if x == "("])
                c = c[noParens:]
                for _ in range(noParens):
                    parens.append(len(waiting))
                try:
                    waiting.append(int(c))
                except ValueError:
                    waiting.append(c)
            elif c.endswith(")"):
                noParens = len([x for x in c if x == ")"])
                waiting.append(int(c[:-noParens]))
                for _ in range(noParens):
                    parenpos = parens.pop()
                    current = waiting[parenpos:]
                    while len(current) >= 2:
                        var0 = current[0]
                        var1 = current[2]
                        op = current[1]
                        if op == "+":
                            current[:3] = [var0 + var1]
                        elif op == "*":
                            current[:3] = [var0 * var1]
                        else:
                            input(f"ERROR: {current}")
                    waiting[parenpos:] = current
            else:
                try:
                    waiting.append(int(c))
                except ValueError:
                    waiting.append(c)
        while len(waiting) >= 2:
            var0 = waiting[0]
            var1 = waiting[2]
            op = waiting[1]
            if op == "+":
                waiting[:3] = [var0 + var1]
            elif op == "*":
                waiting[:3] = [var0 * var1]
            else:
                input("ERROR")
        res += waiting[0]
    return res


def evaluate(current):
    while "+" in current:
        op = current.index("+")
        var0 = current[op-1]
        var1 = current[op+1]
        current[op-1:op+2] = [var0 + var1]
    while "*" in current:
        op = current.index("*")
        var0 = current[op-1]
        var1 = current[op+1]
        current[op-1:op+2] = [var0 * var1]
    return current


def solve_b(data):
    res = 0
    for line in data.splitlines():
        waiting = []
        parens = []
        for c in line.split():
            if c.startswith("("):
                noParens = len([x for x in c if x == "("])
                c = c[noParens:]
                for _ in range(noParens):
                    parens.append(len(waiting))
                try:
                    waiting.append(int(c))
                except ValueError:
                    waiting.append(c)
            elif c.endswith(")"):
                noParens = len([x for x in c if x == ")"])
                waiting.append(int(c[:-noParens]))
                for _ in range(noParens):
                    parenpos = parens.pop()
                    current = waiting[parenpos:]
                    waiting[parenpos:] = evaluate(current)
            else:
                try:
                    waiting.append(int(c))
                except ValueError:
                    waiting.append(c)
        res += evaluate(waiting)[0]
    return res


if __name__ == "__main__":
    main()
