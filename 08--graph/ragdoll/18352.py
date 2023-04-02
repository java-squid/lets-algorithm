import sys

input = sys.stdin.readline

vertex_count, edge_count, distance, begin_vertex = map(int, input().split())

graph = [[] for _ in range(vertex_count + 1)]
visited = [False] * (vertex_count + 1)
for _ in range(edge_count):
    from_vertex, to_vertex = map(int, input().split())
    graph[from_vertex].append(to_vertex)

answers = []


def search(vertex: int, depth: int):
    if depth > distance:
        return

    if depth == distance:
        for v in graph[vertex]:
            if not visited[v]:
                visited[v] = True
                answers.append(v)
        return

    for v in graph[vertex]:
        search(v, depth + 1)


search(begin_vertex, 1)

if not answers:
    answers.append(-1)

for answer in answers:
    print(answer)
