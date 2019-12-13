class PGraph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)
        self.COL = len(graph[0])

    def bfs(self, source, sink, parent):
        visited = [False] * self.ROW
        queue = [source]
        visited[source] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[sink] else False

    def ffa(self, source, sink):
        parent = [-1] * self.ROW
        mflow = 0
        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            mflow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return mflow


def matconstruct(sources, sinks, path):
    epath = []
    lenp = len(path)
    socols = len(sources)
    sicols = len(sinks)
    sink = float("inf")
    epath.append([0] * lenp)
    for i in range(lenp):
        epath.append(path[i])
    epath.append([0] * lenp)
    rowsep = len(epath) - 1
    for i in range(rowsep):
        epath[i].extend([0])
        epath[i].insert(0, 0)
    epath[rowsep].extend([0])
    epath[rowsep].insert(0, 0)
    for i in range(socols):
        sources[i] = sources[i] + 1
    for i in range(sicols):
        sinks[i] = sinks[i] + 1
    for i in range(socols):
        temp = sources[i]
        sumtemp = sum(epath[temp])
        epath[0][temp] = sumtemp
    for i in range(sicols):
        temp = sinks[i]
        epath[temp][rowsep] = sink
    return epath


def solution(entrances, exits, path):
    if len(entrances) == 1 and len(exits) == 1:
        pg = PGraph(path)
        sink = exits[0]
        source = entrances[0]
        mflow = pg.ffa(source, sink)
    else:
        epath = matconstruct(entrances, exits, path)
        pg = PGraph(epath)
        mflow = pg.ffa(0, (len(epath) - 1))
    return mflow
