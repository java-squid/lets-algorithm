import sys

input = sys.stdin.readline


def dfs(index, tree, visited):
    visited[index] = 1
    for i in tree[index]:
        if visited[i] == 0:
            dfs(i, tree, visited)


def solve():
    N, M = map(int, input().split())
    visited = [0] * int(N + 1)  # N >= 1
    tree = [[] for _ in range(N + 1)]  # create list in list

    # 간선 연결 구현
    for _ in range(M):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    count = 0

    for i in range(1, N + 1):
        if visited[i] == 1:
            continue
        count += 1
        dfs(i, tree, visited)

    print(count)


if __name__ == '__main__':
    solve()

# 문제 이해
# 그래프가 주어짐, 연결 요소의 갯수를 구하라 -> 연결 요소란?
# 아마도 노드가 얼마나 연결되어있는지에 대한 갯수를 측정하는듯.
# N은 정점, M은 간선의 갯수
# 간선 ? 줄기가되는 주요선
# 즉 1 2 입력은 1 -> 2로 연결 그러면서 2 -> 1로 연결 되어있고

# 제한 조건
# N은 최대 1000, 그리 많이 않음 시간복잡도는 크게 신경쓰지 않아도 될듯
