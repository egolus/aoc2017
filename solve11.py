from aocd import submit, get_data


def main():
    day = 11
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        "ne,ne,ne": 3,
        "ne,ne,sw,sw": 0,
        "ne,ne,s,s": 2,
        "se,sw,se,sw,sw": 3,
    }
    test_data_b = {
        "": False,
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_a = solve_a(data)
    submit(result_a, part="a", day=day, year=year)

    for i, (test, true) in enumerate(test_data_b.items()):
        result = solve_b(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_b = solve_b(data)
    submit(result_b, part="b", day=day, year=year)


def getDist(coords):
    return (abs(coords[0]) + abs(coords[0] + coords[1]) + abs(coords[1])) // 2


def move(coords, step) -> tuple:
    if step == "n":
        coords = (coords[0], coords[1] - 1)
    if step == "ne":
        coords = (coords[0] + 1, coords[1] - 1)
    if step == "nw":
        coords = (coords[0] - 1, coords[1])
    if step == "s":
        coords = (coords[0], coords[1] + 1)
    if step == "se":
        coords = (coords[0] + 1, coords[1])
    if step == "sw":
        coords = (coords[0] - 1, coords[1] + 1)
    return coords


def solve_a(data):
    coords = (0, 0)
    for step in data.split(","):
        coords = move(coords, step)
    return getDist(coords)


def solve_b(data):
    maxDist = 0
    coords = (0, 0)
    for step in data.split(","):
        coords = move(coords, step)
        maxDist = max(getDist(coords), maxDist)
    return maxDist


if __name__ == "__main__":
    main()
