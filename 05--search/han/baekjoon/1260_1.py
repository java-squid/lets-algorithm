from collections import deque
import sys

input = sys.stdin.readline


def bfs(index, tree, visited):
    visited[index] = 1
    q = deque()
    q.append(index)

    while q:
        node = q.popleft()
        print(node, end=' ')
        tree[node].sort()
        for v in tree[node]:
            if visited[v] == 1:
                continue
            visited[v] = 1
            q.append(v)


def dfs(index, tree, visited):
    visited[index] = 1
    print(index, end=' ')
    tree[index].sort()

    for i in tree[index]:
        if visited[i] == 1:
            continue
        dfs(i, tree, visited)


def solve():
    N, M, V = map(int, input().split())
    visited = [0] * int(N + 1)
    tree = [[] for _ in range(N + 1)]

    for _ in range(M):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    dfs(V, tree, visited)
    print()

    visited = [0] * int(N + 1)
    bfs(V, tree, visited)


if __name__ == '__main__':
    solve()

# 문제 이해
# BFS, DFS 각각 실행한 후에, 그 방문된 점을 print 하는 것

# sudo code
# DFS는 구현했음. 재귀 이용, BFS는 기억 안남..
# BFS 는 큐를 이용함.

# 제한 조건
