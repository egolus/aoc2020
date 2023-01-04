from aocd import submit, get_data
from rich import print as pprint


def main():
    day = 15
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
        "1,3,2": 1,
        "2,1,3": 10,
        "1,2,3": 27,
        "2,3,1": 78,
        "3,2,1": 438,
        "3,1,2": 1836,
    }
    test_data_b = {
        # "0,3,6": 175594,
        # "1,3,2": 2578,
        # "2,1,3": 3544142,
        # "1,2,3": 2661214,
        # "2,3,1": 6895259,
        # "3,2,1": 18,
        # "3,1,2": 362,
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
    numbers = [int(x) for x in data.split(",")]
    pos = len(numbers)-1
    while pos < 2020-1:
        n = numbers[pos]
        instances = [i for i, v in enumerate(numbers) if v == n]
        if len(instances) == 1:
            numbers.append(0)
        else:
            numbers.append(instances[-1] - instances[-2])
        pos += 1
    return numbers[-1]


def isSublist(a, b):
    if 0 == len(a):
        return True

    if len(b) < len(a):
        return False

    idx = -1
    while a[0] in b[idx+1:]:
        idx = b.index(a[0], idx+1)
        if a == b[idx:idx+len(a)]:
            return True

    return False


def solve_b(data):
    sline = data.split(",")
    numbers = {int(x): [i+1] for i, x in enumerate(sline)}
    n = sline[-1]
    for pos in range(len(sline), 30_000_000):
        if n in numbers and len(numbers[n]) > 1:
            n = pos - numbers[n][0]
        else:
            n = 0
        if n not in numbers:
            numbers[n] = []
        elif len(numbers[n]) > 1:
            numbers[n].pop(0)
        numbers[n].append(pos + 1)
        if pos % 100_000 == 0:
            print(f"{pos:_}", end="\r")
        # print(pos, n)
        # pprint(numbers)
        # input()
        if pos > 29_999_990:
            print(pos, n)
    return n


if __name__ == "__main__":
    main()
