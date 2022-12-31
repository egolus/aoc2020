from aocd import submit, get_data


def main():
    day = 9
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
("""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""", 5): 127,
    }
    test_data_b = {
("""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""", 5): 62,  # 15 + 47
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(*test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_a = solve_a(data)
    print(f"result a: {result_a}\n")
    submit(result_a, part="a", day=day, year=year)

    for i, (test, true) in enumerate(test_data_b.items()):
        result = solve_b(*test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_b = solve_b(data)
    print(f"result b: {result_b}\n")
    submit(result_b, part="b", day=day, year=year)


def solve_a(data, preamble=25):
    numbers = []
    for line in data.splitlines():
        numbers.append(int(line))

    for i in range(len(numbers)):
        found = False
        for j in range(i, i+preamble):
            for k in range(j+1, j+preamble):
                if numbers[j] + numbers[k] == numbers[i+preamble]:
                    found = True
                    # break
        if not found:
            return numbers[i+preamble]


def solve_b(data, preamble=25):
    numbers = []
    for line in data.splitlines():
        numbers.append(int(line))

    for i in range(len(numbers)):
        found = False
        for j in range(i, i+preamble):
            for k in range(j+1, j+preamble):
                if numbers[j] + numbers[k] == numbers[i+preamble]:
                    found = True
                    # break
        if not found:
            target = numbers[i+preamble]
            break

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if sum(numbers[i:j+1]) == target:
                return min(numbers[i:j+1]) + max(numbers[i:j+1])
            elif sum(numbers[i:j+1]) > target:
                break


if __name__ == "__main__":
    main()
