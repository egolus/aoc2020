from aocd import submit, get_data


def main():
    day = 4
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""": 2,
}
    test_data_b = {
"""eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""": 0,
"""pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719""": 4,
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
    for block in data.split("\n\n"):
        block = block.replace("\n", " ")

        keys = [b.split(":")[0] for b in block.split()]
        print(keys)
        for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if key not in keys:
                break
        else:
            res += 1
    return res


def solve_b(data):
    res = 0
    for block in data.split("\n\n"):
        block = block.replace("\n", " ")

        print(block)
        for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if key not in [b.split(":")[0] for b in block.split()]:
                break
        else:
            for k, v in [b.split(":") for b in block.split()]:
                try:
                    if k == "byr":
                        if len(v) != 4 or not (1920 <= int(v) <= 2002):
                            print("byr")
                            break
                    if k == "iyr":
                        if len(v) != 4 or not (2010 <= int(v) <= 2020):
                            print("iyr")
                            break
                    if k == "eyr":
                        if len(v) != 4 or not (2020 <= int(v) <= 2030):
                            print("eyr")
                            break
                    if k == "hgt":
                        if not int(v[:-2]) or (v[-2:] not in ("cm", "in")):
                            print("hgt")
                            break
                        elif v[-2:] == "cm" and not (150 <= int(v[:-2]) <= 193):
                            print("hgt")
                            break
                        elif v[-2:] == "in" and not (59 <= int(v[:-2]) <= 76):
                            print("hgt")
                            break
                    if k == "hcl":
                        if v[0] != "#" or len(v) != 7:
                            print("hcl")
                            break
                        for c in v[1:]:
                            if c not in "1234567890abcdef":
                                print("hcl")
                                break
                    if k == "ecl":
                        if v not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                            print("ecl")
                            break
                    if k == "pid":
                        if len(v) != 9 or not int(v):
                            print("pid")
                            break
                except ValueError:
                    print("int conv")
                    break
            else:
                print("valid")
                res += 1
    return res


if __name__ == "__main__":
    main()
