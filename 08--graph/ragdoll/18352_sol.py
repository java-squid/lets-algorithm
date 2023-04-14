import sys
from collections import deque

input = sys.stdin.readline

vertex_count, edge_count, distance, begin_vertex = map(int, input().split())

graph = [[] for _ in range(vertex_count + 1)]
visited = [-1] * (vertex_count + 1)
for _ in range(edge_count):
    from_vertex, to_vertex = map(int, input().split())
    graph[from_vertex].append(to_vertex)

answers = []

def BFS(vertex: int):
    deq = deque()
    deq.append(vertex)
    visited[vertex] += 1
    while deq:
        current = deq.popleft()
        for v in graph[current]:
            if visited[v] == -1:
                visited[v] = visited[current] + 1
                deq.append(v)

BFS(begin_vertex)

for i in range(vertex_count + 1):
    if visited[i] == distance:
        answers.append(i)

if not answers:
    answers.append(-1)

for answer in answers:
    print(answer)
