import sys

input = sys.stdin.readline

N, M = map(int, input().split())
visited = [0] * int(N + 1)
tree = [[] for _ in range(N + 1)]
arrive = False


def dfs(index, depth):
    global arrive

    if depth == 5:
        arrive = True
        return

    visited[index] = 1
    for i in tree[index]:
        if visited[i] == 0:
            dfs(i, depth + 1)
    visited[index] = 0


def solve():
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    depth = 1

    for i in range(N):
        dfs(i, depth)
        if arrive:
            break

    if arrive:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    solve()

# 문제 이해
# 특정 조건에 트리가 매칭되는 지 확인?
# dfs를 이용하는 것 같긴 한데, 어떤 의미인지 모르겠음 왜 예저 2가 통과하는거지? 0 -> 3 -> 2 -> 1 -> 4
# 양쪽으로 연결되어있고 그리고 visited[index] = 0 이 핵심인듯

# 제한 조건
# N은 최대 1000, 그리 많이 않음 시간복잡도는 크게 신경쓰지 않아도 될듯
