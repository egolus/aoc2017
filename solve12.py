from aocd import submit, get_data


def main():
    day = 12
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""": 6,
    }
    test_data_b = {
        """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""": 2,
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


def getGroup(progs, prog, group):
    for other in progs[prog]:
        if other not in group:
            group.append(other)
            getGroup(progs, other, group)
    return group


def solve_a(data):
    progs = {}
    group = ["0"]
    for line in data.splitlines():
        prog, others = line.split(" <-> ")
        progs[prog] = others.split(", ")
    getGroup(progs, "0", group)
    return len(group)


def solve_b(data):
    progs = {}
    groups = []
    for line in data.splitlines():
        prog, others = line.split(" <-> ")
        progs[prog] = others.split(", ")
    toTest = set(progs.keys())
    while toTest:
        prog = toTest.pop()
        group = getGroup(progs, prog, [])
        groups.append(group)
        toTest = toTest.difference(group)
    return len(groups)


if __name__ == "__main__":
    main()
