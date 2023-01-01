from aocd import submit, get_data


def main():
    day = 12
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""F10
N3
F7
R90
F11""": 25,
    }
    test_data_b = {
"""F10
N3
F7
R90
F11""": 286,
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
    position = (0, 0)
    direction = 0
    directions = ("E", "S", "W", "N")

    for line in data.splitlines():
        move, value = line[0], int(line[1:])
        if move == "E" or (move == "F" and direction == 0):
            position = (position[0], position[1] + value)
        elif move == "S" or (move == "F" and direction == 1):
            position = (position[0] + value, position[1])
        elif move == "W" or (move == "F" and direction == 2):
            position = (position[0], position[1] - value)
        elif move == "N" or (move == "F" and direction == 3):
            position = (position[0] - value, position[1])
        elif move == "L":
            direction = (direction - (value // 90)) % len(directions)
        elif move == "R":
            direction = (direction + (value // 90)) % len(directions)

    return sum(abs(p) for p in position)


def solve_b(data):
    position = (0, 0)
    waypoint = (1, 10)

    for line in data.splitlines():
        move, value = line[0], int(line[1:])
        if move == "E":
            waypoint = (waypoint[0], waypoint[1] + value)
        elif move == "S":
            waypoint = (waypoint[0] - value, waypoint[1])
        elif move == "W":
            waypoint = (waypoint[0], waypoint[1] - value)
        elif move == "N":
            waypoint = (waypoint[0] + value, waypoint[1])
        elif move == "L":
            if value == 270:
                waypoint = (waypoint[1] * -1, waypoint[0])
            elif value == 180:
                waypoint = (waypoint[0] * -1, waypoint[1] * -1)
            elif value == 90:
                waypoint = (waypoint[1], waypoint[0] * -1)
        elif move == "R":
            if value == 90:
                waypoint = (waypoint[1] * -1, waypoint[0])
            elif value == 180:
                waypoint = (waypoint[0] * -1, waypoint[1] * -1)
            elif value == 270:
                waypoint = (waypoint[1], waypoint[0] * -1)
        elif move == "F":
            position = (position[0] + value*waypoint[0],
                        position[1] + value*waypoint[1])

    return sum(abs(p) for p in position)


if __name__ == "__main__":
    main()
