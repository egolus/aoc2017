import itertools
from aocd import submit, get_data


def main():
    day = 3
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        "1": 0,
        "6": 1,
        "12": 3,
        "23": 2,
        "1024": 31,
    }
    test_data_b = {
        "3": 4,
        "7": 10,
        "20": 23,
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
    print(f"data: {data}")
    d = int(data)
    if d == 1:
        return 0
    jStop = 1
    for ring, i in enumerate(range(1, d//2, 2)):
        jStart = jStop + 1
        jStop = jStop + (4 + 4 * i)
        if d < jStop:
            minR = ring + 2
            steps = d - jStart
            cc = itertools.cycle(itertools.chain(
                list(reversed(range(minR)))[:-1], list(range(minR))[:-1]))
            next(cc)
            for _ in range(steps + 1):
                s = next(cc)
            return ring + 1 + s


def solve_b(data):
    print(f"data: {data}")
    db = {0: {0: 1}}
    d = int(data)
    cur = 1
    posX = 0
    posY = 0
    directions = ["r", "u", "l", "d"]
    dirPos = 0

    while d >= cur:
        cur = 0
        if directions[dirPos] == "r":
            # go right
            posX += 1
            if posY == 0 or posX > max(db[posY-1].keys()):
                dirPos = (dirPos + 1) % len(directions)
            try:
                cur += db[posY][posX-1]
            except Exception:
                pass
            try:
                cur += db[posY-1][posX-1]
            except Exception:
                pass
            try:
                cur += db[posY-1][posX]
            except Exception:
                pass
            try:
                cur += db[posY-1][posX+1]
            except Exception:
                pass
        elif directions[dirPos] == "u":
            # go up
            posY -= 1
            if posY < min(db.keys()):
                dirPos = (dirPos + 1) % len(directions)
            try:
                cur += db[posY+1][posX-1]
            except Exception:
                pass
            try:
                cur += db[posY][posX-1]
            except Exception:
                pass
            try:
                cur += db[posY-1][posX-1]
            except Exception:
                pass
            try:
                cur += db[posY+1][posX]
            except Exception:
                pass
        elif directions[dirPos] == "l":
            # go left
            posX -= 1
            if posX < min(db[posY+1].keys()):
                dirPos = (dirPos + 1) % len(directions)
            try:
                cur += db[posY+1][posX-1]
            except Exception:
                pass
            try:
                cur += db[posY+1][posX]
            except Exception:
                pass
            try:
                cur += db[posY+1][posX+1]
            except Exception:
                pass
            try:
                cur += db[posY][posX+1]
            except Exception:
                pass
        else:  # directions[dirPos] == "d"
            posY += 1
            if posY > max(db.keys()):
                dirPos = (dirPos + 1) % len(directions)
            try:
                cur += db[posY-1][posX]
            except Exception:
                pass
            try:
                cur += db[posY-1][posX+1]
            except Exception:
                pass
            try:
                cur += db[posY][posX+1]
            except Exception:
                pass
            try:
                cur += db[posY+1][posX+1]
            except Exception:
                pass
        try:
            db[posY][posX] = cur
        except KeyError:
            db[posY] = {posX: cur}
    return cur


if __name__ == "__main__":
    main()
