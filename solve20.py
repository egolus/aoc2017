import re
from aocd import submit, get_data
from pprint import pprint


def main():
    day = 20
    year = 2017
    data = get_data(day=day, year=year)

    test_data_a = {
        """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>""": 0,
    }
    test_data_b = {
        """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>""": 1,
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


def manhatten(point):
    return sum(abs(point[x]) for x in range(3))


def solve_a(data):
    particles = []
    closest = [0, 0]
    for line in data.splitlines():
        p, v, a = line[:-1].split(">, ")
        p = [int(x) for x in p.split("<")[1].split(",")]
        v = [int(x) for x in v.split("<")[1].split(",")]
        a = [int(x) for x in a.split("<")[1].split(",")]
        particles.append({"p": p, "v": v, "a": a})

    while True:
        for p in particles:
            for i in range(3):
                p["v"][i] += p["a"][i]
            for i in range(3):
                p["p"][i] += p["v"][i]
            mdist = manhatten(p["p"])
            p["dt"] = mdist - p.get("dist", 0)
            p["dist"] = mdist

        cl = sorted(enumerate(particles), key=lambda p: p[1]["dt"])[0]
        closest = [cl[0], closest[1]+1 if cl[0] == closest[0] else 0]
        if closest[1] > 100:
            return closest[0]


def solve_b(data):
    particles = {}
    waiting = 0
    for i, line in enumerate(data.splitlines()):
        p, v, a = line[:-1].split(">, ")
        p = [int(x) for x in p.split("<")[1].split(",")]
        v = [int(x) for x in v.split("<")[1].split(",")]
        a = [int(x) for x in a.split("<")[1].split(",")]
        particles[i] = {"p": p, "v": v, "a": a}

    while True:
        for p in particles.values():
            for i in range(3):
                p["v"][i] += p["a"][i]
            for i in range(3):
                p["p"][i] += p["v"][i]
            mdist = manhatten(p["p"])
            p["dt"] = mdist - p.get("dist", 0)
            p["dist"] = mdist

        pop = set()
        for k, v in particles.items():
            for ko, vo in particles.items():
                if k != ko and v["p"] == vo["p"]:
                    pop.add(k)
                    break
        for p in pop:
            particles.pop(p)
        if pop:
            waiting = 0
        else:
            waiting += 1
        if waiting > 100:
            pprint(particles)
            return len(particles)


if __name__ == "__main__":
    main()
