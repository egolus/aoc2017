from aocd import submit, get_data


def main():
    day = 25
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        """Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.""": 3,
    }
    test_data_b = {
        "": True,
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
    tape = set()
    position = 0
    state = "A"
    states = {}
    diag = 0

    cState = "A"
    cVal = 0
    cValMoves = []
    cMoves = {}
    for line in data.splitlines():
        if not line:
            continue
        sline = line.split()
        if line.startswith("Perform a diagnostic checksum after"):
            diag = int(sline[-2])
        elif line.startswith("In state "):
            print(f"cValMoves: {cValMoves}")
            if cValMoves:
                cMoves[cVal] = cValMoves
                cValMoves = []
            print(f"cMoves: {cMoves}")
            if cMoves:
                states[cState] = cMoves
                cMoves = {}
            print(f"states: {states}")
            cState = sline[-1][0]
            print(f"cState: {cState}")
        elif line.startswith("  If the current value is"):
            if cValMoves:
                cMoves[cVal] = cValMoves
                cValMoves = []
            cVal = int(sline[-1][0])
        elif line.startswith("    - Write the value"):
            cValMoves.append(("write", int(sline[-1][0])))
            print(f"cValMoves: {cValMoves}")
        elif line.startswith("    - Move one slot to the"):
            cValMoves.append(("move", sline[-1][:-1]))
            print(f"cValMoves: {cValMoves}")
        elif line.startswith("    - Continue with state"):
            cValMoves.append(("state", sline[-1][:-1]))
            print(f"cValMoves: {cValMoves}")
    if cValMoves:
        cMoves[cVal] = cValMoves
        cValMoves = []
    if cMoves:
        states[cState] = cMoves
        cMoves = {}
    cState = sline[-1][0]

    print(states)

    for step in range(diag):
        prog = states[state]
        for move in prog[int(position in tape)]:
            if move[0] == "write":
                if move[1]:
                    tape.add(position)
                elif position in tape:
                    tape.remove(position)
            elif move[0] == "move":
                if move[1] == "left":
                    position -= 1
                else:
                    position += 1
            elif move[0] == "state":
                state = move[1]
    return len(tape)


def solve_b(data):
    res = 0
    return res


if __name__ == "__main__":
    main()
