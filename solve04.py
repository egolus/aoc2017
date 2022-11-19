import itertools
from aocd import submit, get_data


def main():
    day = 4
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        """aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa""": 2,
    }
    test_data_b = {
        """abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio""": 3,
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


def valid(phrase) -> bool:
    seen = set(phrase.split())
    return len(phrase.split()) == len(seen)


def validAnagram(phrase) -> bool:
    seen = set(str(sorted(x)) for x in phrase.split())
    return len(list(str(sorted(x)) for x in phrase.split())) == len(seen)


def solve_a(data):
    res = 0
    for line in data.splitlines():
        res += valid(line)
    return res


def solve_b(data):
    res = 0
    for line in data.splitlines():
        res += validAnagram(line)
    return res


if __name__ == "__main__":
    main()
