from aocd import submit, get_data


def main():
    day = 5
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        """0
3
0
1
-3""": 5,
    }
    test_data_b = {
        """0
3
0
1
-3""": 10,
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


def solve_a(data):
    res = 0
    pos = 0
    jumps = list(int(x) for x in data.splitlines())
    while pos >= 0 and pos < len(jumps):
        res += 1
        new = jumps[pos]
        jumps[pos] += 1
        pos += new
    return res


def solve_b(data):
    res = 0
    pos = 0
    jumps = list(int(x) for x in data.splitlines())
    while pos >= 0 and pos < len(jumps):
        res += 1
        new = jumps[pos]
        if jumps[pos] >= 3:
            jumps[pos] -= 1
        else:
            jumps[pos] += 1
        pos += new
    return res


if __name__ == "__main__":
    main()
