from collections import deque
import sys

input = sys.stdin.readline


def dfs(index, tree, visited):
    print(index, end=' ')
    visited[index] = 1
    tree[index].sort()

    for v in tree[index]:
        if visited[v] == 0:
            dfs(v, tree, visited)


def bfs(index, tree, visited):
    q = deque()
    q.append(index)
    visited[index] = 1

    while q:
        node = q.popleft()
        print(node, end=' ')
        tree[node].sort()
        for v in tree[node]:
            if visited[v] == 0:
                visited[v] = 1
                q.append(v)


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
# 4 5 1 | 노드 개수 엣지 개수 시작점
# 입력 받은 값을 가지고, DFS로 한번 출력, BFS 한번 출력해야함.
# 중간에 visited 배열을 초기화 해줄 필요 있을듯.

# 제한 조건
# 1<= N <= 1000, 1 <= M <= 10,000

# 참고
# https://seongonion.tistory.com/43
