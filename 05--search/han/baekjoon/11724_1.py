import sys

input = sys.stdin.readline


def dfs(index, tree, visited):
    visited[index] = 1

    for v in tree[index]:
        if visited[v] == 0:
            dfs(v, tree, visited)


def solve():
    N, M = map(int, input().split())
    visited = [0] * int(N + 1)
    tree = [[] for _ in range(N + 1)]

    for _ in range(M):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    count = 0
    for i in range(1, N + 1):
        if visited[i] == 1:
            continue
        dfs(i, tree, visited)
        count += 1
    print(count)


if __name__ == '__main__':
    solve()

# 문제 이해
# 연결 요소
# 예제 입력 1을 기반으로 생각해보면, 1,2,5 -> 1개, 3,4,6 2개 임
# 연결되어있는 요소 가 몇개인지 카운팅하는게 핵심

# 참고
#  1<= N <= 1,000, 1부터 시작하니, for문 돌릴 때 for i in range(1, N + 1) 이렇게 해야할듯