from collections import deque

vertex_count, edge_count, start_vertex = map(int, input().split())

graph = [[] for _ in range(vertex_count + 1)]

dfs_visited = [False] * (vertex_count + 1)
bfs_visited = [False] * (vertex_count + 1)


def DFS(vertex: int) -> None:
    dfs_visited[vertex] = True
    print(vertex, end=' ')

    for adjacent_vertex in graph[vertex]:
        if not dfs_visited[adjacent_vertex]:
            DFS(adjacent_vertex)


bfs_deque = deque()


def BFS(vertex: int) -> None:
    bfs_visited[vertex] = True
    bfs_deque.append(graph[vertex])
    print(vertex, end=' ')

    while len(bfs_deque) > 0:
        vertexes = bfs_deque.popleft()

        for vertex in vertexes:
            if not bfs_visited[vertex]:
                bfs_visited[vertex] = True
                bfs_deque.append(graph[vertex])
                print(vertex, end=' ')


for _ in range(edge_count):
    vertex1, vertex2 = map(int, input().split())
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)

for vertexes in graph:
    vertexes.sort()

DFS(start_vertex)

print()

BFS(start_vertex)
