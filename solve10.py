import functools
from aocd import submit, get_data


def main():
    day = 10
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        ("3,4,1,5", 5): 12,
    }
    test_data_b = {
        "":         "a2582a3a0e66e6e86e3812dcb672a272",
        "AoC 2017": "33efeb34ea91902bb2f59c9920caa6cd",
        "1,2,3":    "3efbe78a8d82f29979031a4aa0b16a9d",
        "1,2,4":    "63960835bcdc130f0b66d7ff4f6a5a8e",
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(*test)
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


def solve_a(data, strLen=256):
    print(data)
    skip = 0
    stringPos = 0
    string = list(range(strLen))

    for l in (int(x) for x in data.split(",")):
        wrap = False
        endWrap = 0
        end = stringPos + l
        part = string[stringPos:end]
        if end > strLen:
            wrap = True
            endWrap = end % strLen
        if wrap:
            part += string[:endWrap]
        part.reverse()
        if wrap:
            string[stringPos:] = part[:-endWrap]
            string[:endWrap] = part[-endWrap:]
        else:
            string[stringPos:end] = part
        stringPos = (end + skip) % strLen
        skip += 1
    return string[0] * string[1]


def solve_b(data, strLen=256):
    print(data)
    skip = 0
    stringPos = 0
    string = list(range(strLen))
    lengths = []
    for c in data:
        lengths.append(ord(c))
    lengths += [17, 31, 73, 47, 23]
    for i in range(64):
        for le in lengths:
            wrap = False
            endWrap = 0
            end = stringPos + le
            part = string[stringPos:end]
            if end > strLen:
                wrap = True
                endWrap = end % strLen
            if wrap:
                part += string[:endWrap]
            part.reverse()
            if wrap:
                string[stringPos:] = part[:-endWrap]
                string[:endWrap] = part[-endWrap:]
            else:
                string[stringPos:end] = part
            stringPos = (end + skip) % strLen
            skip += 1
    binHash = []
    for i in range(16):
        zxor = 0
        [zxor := zxor ^ x for x in string[i*16:(i+1)*16]]
        binHash.append(zxor)
    return "".join(hex(x)[2:].rjust(2, "0") for x in binHash)


if __name__ == "__main__":
    main()
