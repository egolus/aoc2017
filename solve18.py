from aocd import submit, get_data


def main():
    day = 18
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2""": 4,
    }
    test_data_b = {
        """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d""": 3,
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
    registers = {}
    sound = 0
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
        inst, r0, r1 = d[pos]
        try:
            v0 = int(r0)
        except Exception:
            if r0 in registers:
                v0 = registers[r0]
        try:
            v1 = int(r1)
        except Exception:
            if r1 in registers:
                v1 = registers[r1]

        if inst == "snd":
            sound = v0
        elif inst == "set":
            registers[r0] = v1
        elif inst == "add":
            registers[r0] = v0 + v1
        elif inst == "mul":
            registers[r0] = v0 * v1
        elif inst == "mod":
            registers[r0] = v0 % v1
        elif inst == "rcv":
            if v0 and sound:
                return sound
        elif inst == "jgz":
            if v0 > 0:
                pos += v1 - 1
        pos += 1


def solve_b(data):
    res = 0
    registers0 = {"p": 0}
    registers1 = {"p": 1}
    msg0 = []
    msg1 = []
    pos0 = 0
    pos1 = 0
    active = 0
    locked0 = False
    locked1 = False

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
        if locked0 and locked1 and not msg0 and not msg1:
            break
        pos = pos1 if active else pos0
        registers = registers0 if active else registers1
        msgRcv = msg1 if active else msg0
        msgSnd = msg0 if active else msg1

        inst, r0, r1 = d[pos]
        try:
            v0 = int(r0)
        except Exception:
            if r0 in registers:
                v0 = registers[r0]
        try:
            v1 = int(r1)
        except Exception:
            if r1 in registers:
                v1 = registers[r1]

        if inst == "snd":
            msgSnd.append(v0)
            if not active:
                res += 1
        elif inst == "set":
            registers[r0] = v1
        elif inst == "add":
            registers[r0] = v0 + v1
        elif inst == "mul":
            registers[r0] = v0 * v1
        elif inst == "mod":
            registers[r0] = v0 % v1
        elif inst == "rcv":
            if msgRcv:
                if active:
                    locked1 = False
                else:
                    locked0 = False
                registers[r0] = msgRcv.pop(0)
            else:
                active = not active
                if active:
                    locked1 = True
                    pos1 -= 1
                else:
                    locked0 = True
                    pos0 -= 1
        elif inst == "jgz":
            if v0 > 0:
                if active:
                    pos1 += v1 - 1
                else:
                    pos0 += v1 - 1
        if active:
            pos1 += 1
        else:
            pos0 += 1
    return res


if __name__ == "__main__":
    main()
