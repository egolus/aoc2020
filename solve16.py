from aocd import submit, get_data


def main():
    day = 16
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""": 71,
    }
    test_data_b = {
# """class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19

# your ticket:
# 11,12,13

# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9""": -1,
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


def inRanges(ranges, value):
    for r in ranges.values():
        for sr in r:
            if sr[0] <= value <= sr[1]:
                return True
    return False


def solve_a(data):
    res = 0
    ranges = {}

    blocks = data.split("\n\n")
    for line in blocks[0].splitlines():
        name, rest = line.split(":")
        srest = rest.split()
        ranges[name] = []
        ranges[name].append([int(x) for x in srest[0].split("-")])
        ranges[name].append([int(x) for x in srest[2].split("-")])

    for line in blocks[2].splitlines()[1:]:
        for value in line.split(","):
            if not inRanges(ranges, int(value)):
                res += int(value)

    return res


def validRanges(ranges, value):
    valid = set()
    for k, r in ranges.items():
        for sr in r:
            if sr[0] <= value <= sr[1]:
                valid.add(k)
    return valid


def solve_b(data):
    res = 1
    ranges = {}

    blocks = data.split("\n\n")
    positions = {i: set() for i in range(len(blocks[0].splitlines()))}
    for line in blocks[0].splitlines():
        name, rest = line.split(":")
        srest = rest.split()
        ranges[name] = []
        ranges[name].append([int(x) for x in srest[0].split("-")])
        ranges[name].append([int(x) for x in srest[2].split("-")])
        for v in positions.values():
            v.add(name)

    for line in blocks[2].splitlines()[1:]:
        sline = [int(x) for x in line.split(",")]
        for i, value in enumerate(sline):
            valid = validRanges(ranges, value)
            if len(valid) > 0:
                for name in ranges:
                    if name not in valid:
                        positions[i].remove(name)
    for _ in range(len(positions)):
        for k, v in positions.items():
            if len(v) == 1:
                for ok, ov in positions.items():
                    t = list(v)[0]
                    if k != ok and t in ov:
                        ov.remove(t)
    ticket = blocks[1].splitlines()[1].split(",")

    for k, v in positions.items():
        if list(v)[0].startswith("departure"):
            res *= int(ticket[k])
    return res


if __name__ == "__main__":
    main()
