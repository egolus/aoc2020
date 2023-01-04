from itertools import product
from aocd import submit, get_data
from rich import print as pprint


def main():
    day = 14
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""": 165,
    }
    test_data_b = {
"""mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""": 208,
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
    mask = {}
    memory = {}

    for line in data.splitlines():
        sline = line.split()
        if sline[0] == "mask":
            mask = {i: v for i, v in enumerate(sline[2]) if v != "X"}
        elif sline[0].startswith("mem"):
            b = format(int(sline[2]), "036b")
            for k, v in mask.items():
                b = b[0:k] + v + b[k+1:]
            memory[sline[0][4:-1]] = int(b, 2)
    return sum(memory.values())


def solve_b(data):
    mask = {}
    memory = {}

    for line in data.splitlines():
        sline = line.split()
        if sline[0] == "mask":
            mask = {i: v for i, v in enumerate(sline[2]) if v != "0"}
        elif sline[0].startswith("mem"):
            b = format(int(sline[0][4:-1]), "036b")
            for k, v in mask.items():
                b = b[0:k] + v + b[k+1:]
            l = len([v for v in b if v == "X"])
            for it in product(["0", "1"], repeat=l):
                x = b
                for p in it:
                    x = x.replace("X", p, 1)
                memory[x] = int(sline[2])

    return sum(memory.values())


if __name__ == "__main__":
    main()
