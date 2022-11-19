from collections import defaultdict
import re
from aocd import submit, get_data


def main():
    day = 7
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""": "tknk",
    }
    test_data_b = {
        """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""": 60,
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
    ps = {}
    pRe = r"(\w+) \((\d+)\)( -> )*(.*)"
    for line in data.splitlines():
        m = re.match(pRe, line).groups()
        name, weight, children = m[0], m[1], m[3]
        ps[name] = (weight, children.split(", "))
    for it in ps.keys():
        for k, val in ps.items():
            if it in val[1]:
                break
        else:
            return it


def sumUp(ps, item):
    ps[item][1] = sum(sumUp(ps, x) for x in ps[item][2]) + ps[item][0]
    return ps[item][1]


def balance(ps, item):
    weights = [ps[x][1] for x in ps[item][2]]
    counter = defaultdict(int)
    for w in weights:
        counter[w] += 1
    if len(set(counter.values())) > 1:
        rightWeight = sorted(counter.items())[0][0]
        wrongWeight = sorted(counter.items(), reverse=True)[0][0]
        new = balance(ps, next(k for k, v in ps.items() if v[1] == wrongWeight))
        if new:
            return new
        else:
            target = [v for v in ps.values() if v[1] == wrongWeight][0]
            return target[0] + (rightWeight - wrongWeight)


def solve_b(data):
    ps = {}
    pRe = r"(\w+) \((\d+)\)( -> )*(.*)"
    for line in data.splitlines():
        m = re.match(pRe, line).groups()
        name, weight, children = m[0], m[1], m[3]
        ps[name] = [int(weight), int(weight), [x for x in children.split(", ") if x]]
    root = ""
    for it in ps.keys():
        for k, val in ps.items():
            if it in val[2]:
                break
        else:
            root = it
    sumUp(ps, root)
    return balance(ps, root)


if __name__ == "__main__":
    main()
