from aocd import submit, get_data


def main():
    day = 22
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        """..#
#..
...""": 5587,
    }
    test_data_b = {
        """..#
#..
...""": 2511944,
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


def solve_a(data, steps=10_000):
    res = 0
    nodes = set()
    directions = "urdl"
    direction = 0

    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == "#":
                nodes.add((i, j))
    position = (i // 2, j // 2)

    for step in range(steps):
        if position in nodes:
            direction = (direction + 1) % len(directions)
            nodes.remove(position)
        else:
            res += 1
            direction = (direction - 1) % len(directions)
            nodes.add(position)
        if direction == 0:
            position = (position[0] - 1, position[1])
        elif direction == 1:
            position = (position[0], position[1] + 1)
        elif direction == 2:
            position = (position[0] + 1, position[1])
        elif direction == 3:
            position = (position[0], position[1] - 1)
    return res


def solve_b(data, steps=10_000_000):
    res = 0
    infected = set()
    weak = set()
    flagged = set()
    directions = "urdl"
    direction = 0

    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == "#":
                infected.add((i, j))
    position = (i // 2, j // 2)

    for step in range(steps):
        if position in infected:
            direction = (direction + 1) % len(directions)
            infected.remove(position)
            flagged.add(position)
        elif position in weak:
            res += 1
            weak.remove(position)
            infected.add(position)
        elif position in flagged:
            direction = (direction - 2) % len(directions)
            flagged.remove(position)
        else:
            direction = (direction - 1) % len(directions)
            weak.add(position)
        if direction == 0:
            position = (position[0] - 1, position[1])
        elif direction == 1:
            position = (position[0], position[1] + 1)
        elif direction == 2:
            position = (position[0] + 1, position[1])
        elif direction == 3:
            position = (position[0], position[1] - 1)

    return res


if __name__ == "__main__":
    main()
