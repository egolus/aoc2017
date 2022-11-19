from aocd import submit, get_data


def main():
    day = 1
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        "1122": 3,
        "1111": 4,
        "1234": 0,
        "91212129": 9,
    }
    test_data_b = {
        "1212": 6,
        "1221": 0,
        "123425": 4,
        "123123": 12,
        "12131415": 4,
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
    data = data + data[0]
    for i in range(len(data) - 1):
        if data[i] == data[i+1]:
            res += int(data[i])
    return res


def solve_b(data):
    res = 0
    dataRound = data + data
    for i in range(len(data)):
        if data[i] == dataRound[i + len(data) // 2]:
            res += int(data[i])
    return res


if __name__ == "__main__":
    main()
