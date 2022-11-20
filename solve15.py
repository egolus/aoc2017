from aocd import submit, get_data


def main():
    day = 15
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        """Generator A starts with 65
Generator B starts with 8921""": 588,
    }
    test_data_b = {
        """Generator A starts with 65
Generator B starts with 8921""": 309,
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


def solve_a(data, rounds=40_000_000):
    res = 0
    genA = 0
    genB = 0
    factorA = 16807
    factorB = 48271
    divisor = 2147483647
    binA, binB = "", ""
    lines = data.splitlines()
    genA = int(lines[0].split()[-1])
    genB = int(lines[1].split()[-1])
    for i in range(rounds):
        genA = (genA * factorA) % divisor
        binA = bin(genA)[-16:]
        genB = (genB * factorB) % divisor
        binB = bin(genB)[-16:]
        res += binA == binB
    return res


def solve_b(data, rounds=5_000_000):
    res = 0
    genA = 0
    genB = 0
    factorA = 16807
    factorB = 48271
    divisorA = 4
    divisorB = 8
    divisor = 2147483647
    binA, binB = "", ""
    lines = data.splitlines()
    genA = int(lines[0].split()[-1])
    genB = int(lines[1].split()[-1])
    for i in range(rounds):
        while True:
            genA = (genA * factorA) % divisor
            if genA % divisorA:
                continue
            binA = bin(genA)[-16:]
            break
        while True:
            genB = (genB * factorB) % divisor
            if genB % divisorB:
                continue
            binB = bin(genB)[-16:]
            break
        res += binA == binB
    return res


if __name__ == "__main__":
    main()
