from aocd import submit, get_data


def main():
    day = 8
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""": 5,
    }
    test_data_b = {
"""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""": 8,
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
    acc = 0
    prog = []
    done = set()
    pos = 0

    for line in data.splitlines():
        op, val = line.split()
        prog.append((op, int(val)))

    while True:
        if pos >= len(prog):
            break
        if pos in done:
            break
        done.add(pos)
        op, val = prog[pos]
        if op == "acc":
            acc += val
            pos += 1
        if op == "nop":
            pos += 1
        if op == "jmp":
            pos += val
    return acc


def solve_b(data):
    prog = []

    for line in data.splitlines():
        op, val = line.split()
        prog.append((op, int(val)))

    for i in range(len(prog)):
        acc = 0
        done = set()
        pos = 0
        while True:
            if pos >= len(prog):
                return acc
            if pos in done:
                break
            done.add(pos)
            op, val = prog[pos]
            if op == "acc":
                acc += val
                pos += 1
            if op == "nop":
                if pos == i:
                    pos += val
                else:
                    pos += 1
            if op == "jmp":
                if pos == i:
                    pos += 1
                else:
                    pos += val


if __name__ == "__main__":
    main()
