import sys
from collections import deque

input = sys.stdin.readline

vertex_count, edge_count = map(int, input().split())

vertexes = [[] for _ in range(vertex_count + 1)]
visit_count = [0] * (vertex_count + 1)

for _ in range(edge_count):
    from_vertex, to_vertex = map(int, input().split())
    vertexes[from_vertex].append(to_vertex)


def BFS(vertex: int):
    deq = deque()
    deq.append(vertex)

    visited = [False] * (vertex_count + 1)  # 초기화 해야 방문 카운트를 계속 누적 가능

    while deq:
        vertex = deq.popleft()

        for v in vertexes[vertex]:
            if not visited[v]:
                visited[v] = True
                visit_count[v] += 1
                deq.append(v)

for vertex in range(1, vertex_count + 1):
    BFS(vertex)

maximum = 0
for count in visit_count:
    if maximum < count:
        maximum = count

for vertex in range(1, vertex_count + 1):
    if visit_count[vertex] == maximum:
        print(vertex, end=' ')

# 가장 많이 방문된 vertex를 찾아야 함
# 동점이 있는 경우 vertex 번호를 오름차순으로 출력
