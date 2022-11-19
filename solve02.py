import math
from aocd import submit, get_data


def main():
    day = 2
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        """5 1 9 5
7 5 3
2 4 6 8""": 8 + 4 + 6,
    }
    test_data_b = {
        """5 9 2 8
9 4 7 3
3 8 6 5""": 4 + 3 + 2,
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
    for line in data.splitlines():
        m, lo = 0, math.inf
        for c in line.split():
            c = int(c)
            m = max(m, c)
            lo = min(lo, c)
        res += m - lo
    return res


def solve_b(data):
    res = 0
    for line in data.splitlines():
        chars = line.split()
        for i, c in enumerate(chars):
            c = int(c)
            for d in chars[i:]:
                d = int(d)
                if c > d and not c % d:
                    res += c // d
                elif c < d and not d % c:
                    res += d // c
    return res


if __name__ == "__main__":
    main()
