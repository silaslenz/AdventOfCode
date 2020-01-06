f = open("input.txt")
strings = f.readlines()
graph = {}
for string in strings:
    start, _, end, _, dist = string.rstrip().split(" ")
    if start not in graph:
        graph[start] = {}
    if end not in graph:
        graph[end] = {}
    graph[start][end] = int(dist)
    graph[end][start] = int(dist)
print(graph)

all = graph.keys()

def go(graph, visited, at, dist):
    visited.append(at)
    print("going to", at)
    print("visited",visited)
    print("left",graph.keys() - visited)
    if len(graph.keys() - visited) == 0:
        print(dist, visited)
        return dist

    distances = []
    for next in (graph.keys() - visited):
        distances.append(go(graph, list(visited), next, dist + graph[at][next]))
    return max(distances)

distances = []
for start in graph.keys():
    print(start)
    distances.append(go(graph, [], start, 0))
print(distances)
