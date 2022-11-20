import itertools
from aocd import submit, get_data


def main():
    day = 13
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        """0: 3
1: 2
4: 4
6: 4""": 0*3 + 6*4,
    }
    test_data_b = {
        """0: 3
1: 2
4: 4
6: 4""": 10,
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
    scanners = {}
    for line in data.splitlines():
        depth, rng = line.split(": ")
        depth, rng = int(depth), int(rng)
        scanners[depth] = rng
    for d, r in scanners.items():
        if d == 0:
            continue
        if not d % ((r-1)*2):
            res += d*r
    return res


def solve_b(data):
    scanners = {}
    for line in data.splitlines():
        depth, rng = line.split(": ")
        depth, rng = int(depth), int(rng)
        scanners[depth] = rng
    for i in itertools.count(1):
        for d, r in scanners.items():
            if not (d+i) % ((r-1)*2):
                break
        else:
            return i


if __name__ == "__main__":
    main()
