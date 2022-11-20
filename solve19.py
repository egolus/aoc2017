from aocd import submit, get_data
from pprint import pprint


def main():
    day = 19
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ """: "ABCDEF",
    }
    test_data_b = {
        """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ """: 38,
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


def move(maze, position, direction, res):
    y, x = position
    if direction == "d":
        targetPos = (y+1, x)
    elif direction == "u":
        targetPos = (y-1, x)
    elif direction == "r":
        targetPos = (y, x+1)
    elif direction == "l":
        targetPos = (y, x-1)
    target = maze[targetPos[0]][targetPos[1]]
    if target in ["|", "-"]:
        pass
    elif target in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        res.append(target)
    elif target == "+":
        newY, newX = targetPos[0]+1, targetPos[1]
        if (newY, newX) != position and newY in maze and newX in maze[newY]:
            return targetPos, "d", res
        newY, newX = targetPos[0]-1, targetPos[1]
        if (newY, newX) != position and newY in maze and newX in maze[newY]:
            return targetPos, "u", res

        newY, newX = targetPos[0], targetPos[1]-1
        if (newY, newX) != position and newY in maze and newX in maze[newY]:
            return targetPos, "l", res
        newY, newX = targetPos[0], targetPos[1]+1
        if (newY, newX) != position and newY in maze and newX in maze[newY]:
            return targetPos, "r", res
    return targetPos, direction, res


def solve_a(data):
    res = []
    maze = {}
    direction = "d"
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            if c != " ":
                try:
                    maze[y][x] = c
                except Exception:
                    maze[y] = {x: c}
    position = [0, next(k for k in maze[0].keys())]

    while True:
        try:
            position, direction, res = move(maze, position, direction, res)
        except KeyError:
            break

    return "".join(res)


def solve_b(data):
    res = 1
    maze = {}
    direction = "d"
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            if c != " ":
                try:
                    maze[y][x] = c
                except Exception:
                    maze[y] = {x: c}
    position = [0, next(k for k in maze[0].keys())]

    while True:
        try:
            position, direction, _ = move(maze, position, direction, [])
        except KeyError:
            break
        res += 1

    return res


if __name__ == "__main__":
    main()
