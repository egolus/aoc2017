from collections import defaultdict
from aocd import submit, get_data


def main():
    day = 8
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""": 1,
    }
    test_data_b = {
        """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""": 10,
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
    regs = defaultdict(int)
    for line in data.splitlines():
        reg, inst, val, _, other, check, checkVal = line.split()
        do = False
        if check == ">" and regs[other] > int(checkVal):
            do = True
        elif check == "<" and regs[other] < int(checkVal):
            do = True
        elif check == ">=" and regs[other] >= int(checkVal):
            do = True
        elif check == "<=" and regs[other] <= int(checkVal):
            do = True
        elif check == "==" and regs[other] == int(checkVal):
            do = True
        elif check == "!=" and regs[other] != int(checkVal):
            do = True
        if do:
            if inst == "inc":
                regs[reg] += int(val)
            elif inst == "dec":
                regs[reg] -= int(val)
    return max(regs.values())


def solve_b(data):
    maxVal = 0
    regs = defaultdict(int)
    for line in data.splitlines():
        reg, inst, val, _, other, check, checkVal = line.split()
        do = False
        if check == ">" and regs[other] > int(checkVal):
            do = True
        elif check == "<" and regs[other] < int(checkVal):
            do = True
        elif check == ">=" and regs[other] >= int(checkVal):
            do = True
        elif check == "<=" and regs[other] <= int(checkVal):
            do = True
        elif check == "==" and regs[other] == int(checkVal):
            do = True
        elif check == "!=" and regs[other] != int(checkVal):
            do = True
        if do:
            if inst == "inc":
                regs[reg] += int(val)
            elif inst == "dec":
                regs[reg] -= int(val)
            maxVal = max(regs[reg], maxVal)
    return maxVal


if __name__ == "__main__":
    main()
