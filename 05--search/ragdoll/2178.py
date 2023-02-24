from collections import deque

# BFS를 사용한다. (인접칸 숫자가 1이고 방문하지 않았으면 큐에 삽입)
# => 특정 깊이를 완전 탐색 이후 다음 깊이를 탐색하기 때문에 최단거리 탐색에 적합하다.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

row_count, column_count = map(int, input().split())
table = [[0] * column_count for _ in range(row_count)]
visited = [[False] * column_count for _ in range(row_count)]


def BFS(row_number: int, column_number: int) -> None:
    queue = deque()
    visited[row_number][column_number] = True
    queue.append((row_number, column_number))

    while queue:
        current = queue.popleft()

        for i in range(4):
            x = current[0] + dx[i]
            y = current[1] + dy[i]

            if 0 <= x < row_count and 0 <= y < column_count:
                if table[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    table[x][y] = table[current[0]][current[1]] + 1
                    queue.append((x, y))


for i in range(0, row_count):
    input_numbers = list(map(int, list(input())))

    for j in range(0, column_count):
        table[i][j] = input_numbers[j]

BFS(0, 0)

print(table[row_count - 1][column_count - 1])
