from aocd import submit, get_data


def main():
    day = 7
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""": 4,
}
    test_data_b = {
"""light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""": 32,
"""shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""": 126,
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


def getOthers(bags, bag):
    f = {k: 0 for k in bags}
    again = True
    while again:
        again = False
        for k, v in bags.items():
            if f[k] == 2:
                continue
            if bag in v:
                again = True
                f[k] = 1
        for l, w in f.items():
            if w == 1:
                for k, v in bags.items():
                    if f[k] == 2:
                        continue
                    if l in v:
                        again = True
                        f[k] = 1
                f[l] = 2
    return f


def solve_a(data):
    bags = {}
    for line in data.splitlines():
        sline = line.split()
        bag = " ".join(sline[:2])
        others = []
        for i in range(5, len(sline), 4):
            if sline[i:i+2] != ["other", "bags."]:
                others.append(" ".join(sline[i:i+2]))
        bags[bag] = others
    f = getOthers(bags, "shiny gold")
    return sum(True for x in f.values() if x)


def getContent(bags, bag):
    res = 0
    for o, i in bags[bag]:
        res += i + i * getContent(bags, o)
    return res


def solve_b(data):
    bags = {}
    for line in data.splitlines():
        sline = line.split()
        bag = " ".join(sline[:2])
        others = []
        for i in range(5, len(sline), 4):
            if sline[i:i+2] != ["other", "bags."]:
                others.append((" ".join(sline[i:i+2]), int(sline[i-1])))
        bags[bag] = others
    return getContent(bags, "shiny gold")


if __name__ == "__main__":
    main()
