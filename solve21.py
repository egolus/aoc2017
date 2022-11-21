import math
from aocd import submit, get_data


def main():
    day = 21
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        ("""../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#""", 2): 12,
    }
    test_data_b = {
        ("""../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#""", 2): 12,
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(*test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_a = solve_a(data)
    submit(result_a, part="a", day=day, year=year)

    for i, (test, true) in enumerate(test_data_b.items()):
        result = solve_b(*test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_b = solve_b(data)
    submit(result_b, part="b", day=day, year=year)


def rotate(square, times=1):
    old = tuple(square)
    for _ in range(times):
        cols = []
        for i in range(1, len(square) + 1):
            cols.append(tuple(old[j][-i] for j in range(len(old))))
        old = tuple(cols)
    return old


def flip(square, horizontal=False):
    if horizontal:
        cols = []
        for r in square:
            cols.append(tuple(reversed(r)))
    else:
        cols = reversed(square)
    return tuple(cols)


def solve_a(data, iterations=5):
    rules = {}
    square = []
    square.append([False, True, False])
    square.append([False, False, True])
    square.append([True, True, True])

    for line in data.splitlines():
        i, o = line.split(" => ")
        i, o = ((tuple(i.split("/")), tuple(o.split("/"))))
        i = tuple(tuple((True if x == "#" else False) for x in j) for j in i)
        o = tuple(tuple((True if x == "#" else False) for x in j) for j in o)
        rules[i] = o
        for j in range(1, 4):
            rot = rotate(i, j)
            if rot not in rules:
                rules[rot] = o
        flp = flip(i)
        if flp not in rules:
            rules[flp] = o
        for j in range(1, 4):
            rot = rotate(flp, j)
            if rot not in rules:
                rules[rot] = o
        flp = flip(i, horizontal=True)
        if flp not in rules:
            rules[flp] = o
        for j in range(1, 4):
            rot = rotate(flp, j)
            if rot not in rules:
                rules[rot] = o

    for it in range(iterations):
        new = []
        if not len(square) % 2:
            # 2 -> 3
            div = 2
            newDiv = 3
        else:
            # 3 -> 2
            div = 3
            newDiv = 4
        newPosY = 0

        for _ in range(len(square) // div * newDiv):
            new.append([])

        for posY in range(0, len(square), div):
            for posX in range(0, len(square), div):
                window = []
                for row in square[posY:posY+div]:
                    window.append(tuple(row[posX:posX+div]))
                window = tuple(window)
                newWindow = rules[window]
                for i, row in enumerate(newWindow):
                    new[newPosY+i] += row
            newPosY += newDiv
        square = new

    return sum(sum(row) for row in square)


def solve_b(data, iterations=18):
    rules = {}
    square = []
    square.append([False, True, False])
    square.append([False, False, True])
    square.append([True, True, True])

    for line in data.splitlines():
        i, o = line.split(" => ")
        i, o = ((tuple(i.split("/")), tuple(o.split("/"))))
        i = tuple(tuple((True if x == "#" else False) for x in j) for j in i)
        o = tuple(tuple((True if x == "#" else False) for x in j) for j in o)
        rules[i] = o
        for j in range(1, 4):
            rot = rotate(i, j)
            if rot not in rules:
                rules[rot] = o
        flp = flip(i)
        if flp not in rules:
            rules[flp] = o
        for j in range(1, 4):
            rot = rotate(flp, j)
            if rot not in rules:
                rules[rot] = o
        flp = flip(i, horizontal=True)
        if flp not in rules:
            rules[flp] = o
        for j in range(1, 4):
            rot = rotate(flp, j)
            if rot not in rules:
                rules[rot] = o

    for it in range(iterations):
        new = []
        if not len(square) % 2:
            # 2 -> 3
            div = 2
            newDiv = 3
        else:
            # 3 -> 2
            div = 3
            newDiv = 4
        newPosY = 0

        for _ in range(len(square) // div * newDiv):
            new.append([])

        for posY in range(0, len(square), div):
            for posX in range(0, len(square), div):
                window = []
                for row in square[posY:posY+div]:
                    window.append(tuple(row[posX:posX+div]))
                window = tuple(window)
                newWindow = rules[window]
                for i, row in enumerate(newWindow):
                    new[newPosY+i] += row
            newPosY += newDiv
        square = new

    return sum(sum(row) for row in square)


if __name__ == "__main__":
    main()
