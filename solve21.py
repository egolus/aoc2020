from aocd import submit, get_data
from functools import reduce


def main():
    day = 21
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""": 5,
}
    test_data_b = {
"""mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""": "mxmxvkd,sqjhc,fvjkl",
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
    allergens = {}
    ingredients = {}

    for line in data.splitlines():
        ins, als = line.split("(")
        ins = ins.split()
        als = [al.replace(",", "").replace(")", "") for al in als.split() if al != "contains"]
        for al in als:
            if al in allergens:
                allergens[al].append(set(ins))
            else:
                allergens[al] = [set(ins)]
        for ing in ins:
            if ing in ingredients:
                ingredients[ing] += 1
            else:
                ingredients[ing] = 1

    while allergens:
        for k, v in list(allergens.items()):
            if len(res := reduce(lambda x, y: x.intersection(y), v)) == 1:
                ing = res.pop()
                allergens.pop(k)
                ingredients.pop(ing)
                for av in allergens.values():
                    for avv in av:
                        avv.discard(ing)

    return sum(ingredients.values())


def solve_b(data):
    allergens = {}
    ingredients = {}

    for line in data.splitlines():
        ins, als = line.split("(")
        ins = ins.split()
        als = [al.replace(",", "").replace(")", "") for al in als.split() if al != "contains"]
        for al in als:
            if al in allergens:
                allergens[al].append(set(ins))
            else:
                allergens[al] = [set(ins)]

    while allergens:
        for k, v in list(allergens.items()):
            if len(res := reduce(lambda x, y: x.intersection(y), v)) == 1:
                ing = res.pop()
                ingredients[ing] = k
                allergens.pop(k)
                for av in allergens.values():
                    for avv in av:
                        avv.discard(ing)

    return ",".join(k for k, v in sorted(ingredients.items(), key=lambda x: x[1]))

if __name__ == "__main__":
    main()
