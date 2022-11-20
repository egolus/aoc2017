from aocd import submit, get_data


def main():
    day = 16
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        ("s1,x3/4,pe/b", 5): "baedc",
    }
    test_data_b = {
        ("s1,x3/4,pe/b", 5, 2): "ceadb",
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(*test)
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


def solve_a(data, count=16):
    d = list("abcdefghijklmnop"[:count])

    for move in data.split(","):
        if move[0] == "s":
            # spin
            for _ in range(int(move[1:])):
                d = [d[-1]] + d[:-1]
        elif move[0] == "x":
            # exchange
            p0, p1 = [int(x) for x in move[1:].split("/")]
            d[p0], d[p1] = d[p1], d[p0]
        elif move[0] == "p":
            # partner
            n0, n1 = move[1:].split("/")
            p0 = d.index(n0)
            p1 = d.index(n1)
            d[p0], d[p1] = d[p1], d[p0]
    return "".join(d)


def solve_b(data, count=16, rounds=1_000_000_000):
    d = list("abcdefghijklmnop"[:count])
    rest = rounds

    while rest:
        for r in range(rest):
            for move in data.split(","):
                if move[0] == "s":
                    # spin
                    for _ in range(int(move[1:])):
                        d = [d[-1]] + d[:-1]
                elif move[0] == "x":
                    # exchange
                    p0, p1 = [int(x) for x in move[1:].split("/")]
                    d[p0], d[p1] = d[p1], d[p0]
                elif move[0] == "p":
                    # partner
                    n0, n1 = move[1:].split("/")
                    p0 = d.index(n0)
                    p1 = d.index(n1)
                    d[p0], d[p1] = d[p1], d[p0]
            if d == list("abcdefghijklmnop"[:count]):
                rest = rest % (r+1)
                break
        else:
            break

    return "".join(d)


if __name__ == "__main__":
    main()
