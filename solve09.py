from aocd import submit, get_data


def main():
    day = 9
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        "{}": 1,
        "{{{}}}": 1+2+3,
        "{{},{}}": 1+2+2,
        "{{{},{},{{}}}}": 1+2+3+3+3+4,
        "{<a>,<a>,<a>,<a>}": 1,
        "{{<ab>},{<ab>},{<ab>},{<ab>}}": 1+2+2+2+2,
        "{{<!!>},{<!!>},{<!!>},{<!!>}}": 1+2+2+2+2,
        "{{<a!>},{<a!>},{<a!>},{<ab>}}": 1+2,
    }
    test_data_b = {
        "<>": 0,
        "<random characters>": 17,
        "<<<<>": 3,
        "<{!>}>": 2,
        "<!!>": 0,
        "<!!!>>": 0,
        """<{o"i!a,<{i<a>""": 10,
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
    grp = 0
    store = []
    garbage = False
    d = iter(data)
    for c in d:
        if c == "{" and not garbage:
            grp += 1
            store.append(c)
        elif c == "}" and not garbage:
            while store:
                if store.pop(-1) == "{":
                    res += grp
                    grp -= 1
                    break
        elif c == "<":
            garbage = True
        elif c == ">":
            garbage = False
        elif c == "!":
            next(d)
    return res


def solve_b(data):
    res = 0
    grp = 0
    store = []
    garbage = False
    d = iter(data)
    for c in d:
        if c == ">":
            garbage = False
        elif c == "!":
            next(d)
        elif garbage:
            res += 1
        elif c == "<":
            garbage = True
        elif c == "{" and not garbage:
            grp += 1
            store.append(c)
        elif c == "}" and not garbage:
            while store:
                if store.pop(-1) == "{":
                    grp -= 1
                    break
    return res


if __name__ == "__main__":
    main()
