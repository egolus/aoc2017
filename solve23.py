import math
from aocd import submit, get_data


def main():
    day = 23
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        # "": True,
    }
    test_data_b = {
        # "": True,
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
    registers = {}
    pos = 0
    r0, r1 = 0, 0
    v0, v1 = 0, 0

    d = []

    for line in data.splitlines():
        try:
            inst, r0, r1 = line.split()
        except Exception:
            inst, r0 = line.split()
        d.append((inst, r0, r1))

    while True:
        if pos < 0 or pos >= len(d):
            break
        inst, r0, r1 = d[pos]
        try:
            v0 = int(r0)
        except Exception:
            if r0 in registers:
                v0 = registers[r0]
            else:
                v0 = 0
        try:
            v1 = int(r1)
        except Exception:
            if r1 in registers:
                v1 = registers[r1]
            else:
                v0 = 0

        if inst == "set":
            registers[r0] = v1
        elif inst == "sub":
            registers[r0] = v0 - v1
        elif inst == "mul":
            res += 1
            registers[r0] = v0 * v1
        elif inst == "jnz":
            if v0 != 0:
                pos += v1 - 1
        pos += 1
    return res


def isPrime(num):
    for i in range(2, int(math.sqrt(num))):
        if not num % i:
            return False
    return num != 1


def solve_b(data):
    h = 0
    # I should at least get the three values from the input ..
    for b in range(105700, 122701, 17):
        if not isPrime(b):
            h += 1
    return h


if __name__ == "__main__":
    main()
