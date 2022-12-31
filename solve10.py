from aocd import submit, get_data
from rich import print as pprint


def main():
    day = 10
    year = 2020
    data = get_data(day=day, year=year)

    test_data_a = {
"""16
10
15
5
1
11
7
19
6
12
4""": 7*5,
"""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""": 220,
    }
    test_data_b = {
"""16
10
15
5
1
11
7
19
6
12
4""": 8,
"""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""": 19208,
    }

    for i, (test, true) in enumerate(test_data_a.items()):
        result = solve_a(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_a = solve_a(data)
    print(f"result a: {result_a}\n")
    submit(result_a, part="a", day=day, year=year)

    for i, (test, true) in enumerate(test_data_b.items()):
        result = solve_b(test)
        print(f"result {i}: {result}\n")
        assert result == true, f"{result} != {true}"

    result_b = solve_b(data)
    print(f"result b: {result_b}\n")
    submit(result_b, part="b", day=day, year=year)


def solve_a(data):
    adapters = [0]

    for line in data.splitlines():
        adapters.append(int(line))
    adapters = sorted(adapters)

    adapters.append(adapters[-1]+3)
    pprint(adapters)

    ones = 0
    threes = 0
    for i in range(len(adapters)-1):
        if adapters[i+1] - adapters[i] == 1:
            ones += 1
        elif adapters[i+1] - adapters[i] == 3:
            threes += 1

    return ones * threes


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, u, v):
        self.adj[u].append(v)

    def countPaths(self, s, d):
        visited = [False] * self.V
        pathCount = [0]
        self.countPathsUtil(s, d, visited, pathCount)
        return pathCount[0]

    def countPathsUtil(self, u, d, visited, pathCount):
        visited[u] = True
        if (u == d):
            pathCount[0] += 1
        else:
            i = 0
            while i < len(self.adj[u]):
                if (not visited[self.adj[u][i]]):
                    self.countPathsUtil(self.adj[u][i], d, visited, pathCount)
                i += 1
            print(pathCount, end="\r")
        visited[u] = False


def getChain(adapters):
    graph = Graph(max(adapters)+1)
    for ad in adapters:
        for j in range(1, 4):
            if ad + j in adapters:
                graph.addEdge(ad, ad+j)
    pprint(graph.adj)
    return graph.countPaths(0, adapters[-1])


def solve_b(data):
    res = 1
    adapters = [0]

    for line in data.splitlines():
        adapters.append(int(line))
    adapters = sorted(adapters)

    adapters.append(adapters[-1]+3)
    pprint(adapters)

    res = getChain(adapters)
    return res


if __name__ == "__main__":
    main()
