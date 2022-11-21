from aocd import submit, get_data


def main():
    day = 24
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10""": 31,
    }
    test_data_b = {
        """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10""": 19,
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


def chain(comps, chn=[], end=0, longest=0):
    for c in [x for x in comps if end in x and x not in chn]:
        ln = chain(comps, chn + [c], c[1] if c[0] == end else c[0], longest)
        longest = max(longest, ln)
    else:
        return max(longest, sum(sum(c) for c in chn))
    return longest


def solve_a(data):
    comps = []
    for line in data.splitlines():
        a, b = line.split("/")
        comps.append((int(a), int(b)))
    print(comps)
    return chain(comps)


def chain_b(comps, chn=[], end=0, longest=None):
    if longest is None:
        longest = []
    for c in [x for x in comps if end in x and x not in chn]:
        ln = chain_b(comps, chn + [c], c[1] if c[0] == end else c[0], longest)
        if [(0, 2), (2, 2), (2, 3), (3, 4)] in [ln, longest]:
            print(ln, longest)
        if len(ln) > len(longest):
            longest = ln
        elif len(ln) == len(longest):
            if sum(sum(c) for c in ln) > sum(sum(c) for c in longest):
                longest = ln
    else:
        if [(0, 2), (2, 2), (2, 3), (3, 4)] in [chn, longest]:
            print(chn, longest)
        if len(chn) > len(longest):
            return chn
        elif len(chn) == len(longest):
            if sum(sum(c) for c in chn) > sum(sum(c) for c in longest):
                return chn
    return longest


def solve_b(data):
    comps = []
    for line in data.splitlines():
        a, b = line.split("/")
        comps.append((int(a), int(b)))
    print(comps)
    ln = chain_b(comps)
    print(ln, sum(sum(c) for c in ln))
    return sum(sum(c) for c in ln)


if __name__ == "__main__":
    main()
