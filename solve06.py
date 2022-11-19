from aocd import submit, get_data


def main():
    day = 6
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        "0	2	7	0": 5,
    }
    test_data_b = {
        "0	2	7	0": 4,
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
    banks = list(int(x) for x in data.split())
    bankIndex = 0
    old = []
    while tuple(banks) not in old:
        res += 1
        old.append(tuple(banks))
        cur = max(banks)
        bankIndex = banks.index(cur)
        banks[bankIndex] = 0
        while cur > 0:
            cur -= 1
            bankIndex = (bankIndex + 1) % len(banks)
            banks[bankIndex] += 1
    return res


def solve_b(data):
    banks = list(int(x) for x in data.split())
    bankIndex = 0
    for i in range(2):
        res = 0
        old = []
        while tuple(banks) not in old:
            res += 1
            old.append(tuple(banks))
            cur = max(banks)
            bankIndex = banks.index(cur)
            banks[bankIndex] = 0
            while cur > 0:
                cur -= 1
                bankIndex = (bankIndex + 1) % len(banks)
                banks[bankIndex] += 1
    return res


if __name__ == "__main__":
    main()
