from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, - 1, 0]


def solve():
    N, M = map(int, input().split())
    maze = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        row = input().strip()
        for j in range(M):
            maze[i][j] = int(row[j])

    # BFS
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1

    while q:
        index = q.popleft()
        for k in range(4):
            x = index[0] + dx[k]
            y = index[1] + dy[k]
            if 0 <= x < N and 0 <= y < M:
                if maze[x][y] != 0 and visited[x][y] == 0:
                    visited[x][y] = 1
                    maze[x][y] = maze[index[0]][index[1]] + 1
                    q.append([x, y])

    print(maze[N - 1][M - 1])


if __name__ == '__main__':
    solve()

# 문제 이해
# 미로에서 1은 지나갈 수 있고, 0은 지나갈 수 없음
# 이동은 인접한 칸만 가능
# 출발은 항상 1,1
# 출발 부터 특정 위치 N,M 까지

# sudo code
# maze input
# BFS 를 어떻게 돌리고, 가장 최소값을 고를지 생각나지 않았음


# 제한 조건
# 크게 신경쓸 조건은 없는듯

# 참고
