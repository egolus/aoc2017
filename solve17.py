from aocd import submit, get_data


def main():
    day = 17
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        "3": 638,
    }
    test_data_b = {
        ("3", 2018): 1226,
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_a = solve_a(data)
    submit(result_a, part="a", day=day, year=year)

    for i, (test, true) in enumerate(test_data_b.items()):
        result = solve_b(*test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_b = solve_b(data)
    submit(result_b, part="b", day=day, year=year)


def solve_a(data, rounds=2018):
    lock = [0]
    pos = 0
    steps = int(data)

    for r in range(1, rounds):
        pos = ((pos + steps) % len(lock)) + 1
        lock.insert(pos, r)
        if r < 10:
            print(pos)
    print(lock[1], len(lock))
    return lock[pos+1]


def solve_b(data, rounds=50_000_000):
    res = 0
    pos = 0
    steps = int(data)

    for r in range(1, rounds):
        pos = ((pos + steps) % (r)) + 1
        if pos == 1:
            res = r
        if r < 10:
            print(pos)
    return res


if __name__ == "__main__":
    main()
