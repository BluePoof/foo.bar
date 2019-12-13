import itertools

enumeration = []


def enum(times):
    for u, row, in enumerate(times):
        for v, w, in enumerate(row):
            yield (u, v, w)


def bellmanford(times):
    tmatrix = []
    for i in range(len(times)):

        def subbellmanford(times, start):
            subtime = [float("inf") for each in times]
            subtime[start] = times[start][start]
            for each in range(len(times)):
                for u, v, w, in enumeration:
                    if subtime[u] + w < subtime[v]:
                        subtime[v] = subtime[u] + w
            return subtime

        time = subbellmanford(times, i)
        tmatrix.append(time)
    return tmatrix


def calctime(bunnies, tmatrix):
    time = 0
    for i in range(len(bunnies) - 1):
        startbun = bunnies[i]
        nextbun = bunnies[i + 1]
        time += tmatrix[startbun][nextbun]
    start = 0
    bulkhead = len(tmatrix) - 1
    time += (tmatrix[start][bunnies[0]] + tmatrix[bunnies[-1]][bulkhead])
    return time


def solution(times, times_limit):
    global enumeration
    enumeration = [x for x in enum(times)]
    nbunnies = len(times) - 2
    bindex = [bunnies + 1 for bunnies in range(nbunnies)]
    tmatrix = bellmanford(times)

    def checknegcycle(matrix):
        times = matrix[0]
        for u, v, w in enumeration:
            if times[u] + w < times[v]:
                return True
        return False

    if checknegcycle(tmatrix):
        return list(range(nbunnies))
    for i in range(nbunnies, 0, -1):
        for p in itertools.permutations(bindex, i):
            time = calctime(p, tmatrix)
            if time <= times_limit:
                return [bunnies - 1 for bunnies in sorted(p)]
