# Python3로 실행하면 recursion error 발생, PyPy3로 채점하면 통과
# 모든 노드를 탐색 하는 데에 실행한 DFS 횟수 == 하나의 연결요소 수
import sys

sys.setrecursionlimit(1_000)
node_count, edge_count = map(int, input().split())
graph = [[] for _ in range(node_count + 1)]  # graph = [[]] * (node_count + 1) 이렇게 선언하면 얕은 복사 되어 기대 값대로 동작 안됨
visited = [False] * (node_count + 1)
dfs_count = 0


def DFS(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            DFS(i)


for i in range(edge_count):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for node in range(1, node_count + 1):
    if not visited[node]:
        dfs_count += 1
        DFS(node)

print(dfs_count)
