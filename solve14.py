from aocd import submit, get_data


def main():
    day = 14
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        "flqrgnkx": 8108,
    }
    test_data_b = {
        "flqrgnkx": 1242,
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


def knotHash(data, strLen=256):
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


def clearGroup(binHashes, y, x):
    if y > 0 and binHashes[y-1][x]:
        binHashes[y-1][x] = False
        clearGroup(binHashes, y-1, x)
    if y < len(binHashes)-1 and binHashes[y+1][x]:
        binHashes[y+1][x] = False
        clearGroup(binHashes, y+1, x)
    if x > 0 and binHashes[y][x-1]:
        binHashes[y][x-1] = False
        clearGroup(binHashes, y, x-1)
    if x < len(binHashes)-1 and binHashes[y][x+1]:
        binHashes[y][x+1] = False
        clearGroup(binHashes, y, x+1)


def solve_a(data):
    res = 0
    for i in range(128):
        d = data + f"-{i}"
        dHash = knotHash(d)
        binHash = "".join(bin(int(x, base=16))[2:].rjust(4, "0") for x in dHash)
        res += binHash.count("1")
    return res


def solve_b(data):
    regions = 0
    binHashes = {}
    for i in range(128):
        d = data + f"-{i}"
        dHash = knotHash(d)
        binHash = "".join(bin(int(x, base=16))[2:].rjust(4, "0") for x in dHash)
        binHashes[i] = {}
        for j, b in enumerate(binHash):
            binHashes[i][j] = bool(int(b))

    for y in binHashes.keys():
        for x in binHashes[y].keys():
            if binHashes[y][x]:
                regions += 1
                binHashes[y][x] = False
                clearGroup(binHashes, y, x)
    return regions


if __name__ == "__main__":
    main()
