from collections import deque
import sys

input = sys.stdin.readline


def bfs(v, visited, A, distance):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        node = q.popleft()
        for e, v in A[node]:
            if not visited[e]:
                visited[e] = True
                q.append(e)
                distance[e] = distance[node] + v


def solve():
    N = int(input())
    A = [[] for _ in range(N + 1)]
    distance = [0] * (N + 1)
    visited = [False] * (N + 1)

    for _ in range(N):
        # 1 3 2 -1
        d = list(map(int, input().split()))
        i = 0
        S = d[i]  # 1, i = 0
        i += 1  # i = 1
        while True:
            E = d[i]  # 3, i = 1
            if E == -1:
                # 제약조건 -1이면 연결된 노드가 없다는 뜻. 더 이상 연결노드 추가하지 않아도됨.
                break
            V = d[i + 1]  # 2, i = 1
            A[S].append((E, V))  # tuple 형태로 연결된 노드 추가
            i += 2  # i = 3

    bfs(1, visited, A, distance)

    temp = 1

    for i in range(2, N + 1):
        if distance[temp] < distance[i]:
            temp = i

    distance = [0] * (N + 1)
    visited = [False] * (N + 1)
    bfs(temp, visited, A, distance)
    distance.sort()
    print(distance[N])


if __name__ == '__main__':
    solve()

# 문제 이해
# 입력 312 -> 3 노드 - 2 - 1 노드
# 노드는 튜플로 선언 왜? 어떤 노드가 얼마나 거리가 먼 엣지와 연결되어있는지 알기 위해선
# 최대 거리를 측정할 배열과, 방문을 확인할 배열이 필요할듯.
# 어렵다, 더 이상 어떻게 풀어나가야할지 모르겠음. -> 답안 확인

# 제약사항
# 노드 갯수는 2 이상
# 입력된 수중에 -1이면 연결된 노드가 없다는 뜻.
