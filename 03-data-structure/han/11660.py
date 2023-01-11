# https://www.acmicpc.net/problem/11660

import sys

input = sys.stdin.readline


# def solve():
nm = list(input().split())
n = int(nm[0])
m = int(nm[1])
A = [[0] * (n + 1)]
D = [[0] * (n + 1) for _ in range(n + 1)]  # _ -> dummy variable

# 원본 리스트 저장
for i in range(n):
    row = [0] + [int(x) for x in input().split()]
    A.append(row)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j], 이걸 생각해낼수 있었을까?
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1])


if __name__ == '__main__':
    solve()

# 풀이
# 4 3 n = 4, 4x4 배열, m = 3 질의 갯수
# 1 2 3 4 배열
# 2 3 4 5 배열
# 3 4 5 6 배열
# 4 5 6 7 배열
# 2 2 3 4 질의
# 3 4 3 4 질의
# 1 1 4 4 질의

# prefix_sum 이용
