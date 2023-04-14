from collections import deque
import sys

input = sys.stdin.readline

def bfs(v, visited, A):
    q = deque()
    q.append(v)
    visited[v] += 1

    while q:
        node = q.popleft()
        for i in A[node]:
            if visited[i] == -1:
                visited[i] = visited[node] + 1
                q.append(i)

def solve():
    N, M, K, X = map(int, input().split())
    A = [[] for _ in range(N + 1)] # 도시의 연결을 나타내기 위한 배열, 도시는 1부터 시작하니 크기는 N + 1 만큼
    result = []
    visited = [-1] * (N + 1) # 방문 했는 지 확인

    for _ in range(M):
        S, E = map(int, input().split())
        A[S].append(E)

    # X 출발 도시 번호
    bfs(X, visited, A)

    for i in range(N + 1):
        if visited[i] == K:
            result.append(i)

    if not result:
        print(-1)
    else:
        result.sort()
        for i in result:
            print(i)


if __name__ == '__main__':
    solve()

# 문제 이해
# 단방향으로만 이동할 수 있음.
# 최단거리 문제, K가 주어짐. 정확히 K랑 같은 거리인 노드만 찾으면 됨.
# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
# BFS이용하면 될 것 같은데.. 잘 안됨 -> 답안 참고

