#===================================================
#
# import sys
#
# input = sys.stdin.readline
# size, calculation_count = map(int, input().split())
# MIN_INDEX = 0
# MAX_INDEX = size - 1
#
# table = []
# sum = 0
# for i in range(size):
#     row = []
#
#     numbers = map(int, input().split())
#     for number in numbers:
#         sum += number
#         row.append(sum)
#
#     table.append(row)
#
#
# def previous_index(x: int, y: int) -> list:
#     if y - 1 < MIN_INDEX:
#         return [x - 1, MAX_INDEX]
#
#     return [x, y - 1]
#
#
# for i in range(calculation_count):
#     x1, y1, x2, y2 = [int(point_x_y) - 1 for point_x_y in input().split()]
#
#     previous_x1, previous_y1 = previous_index(x1, y1)
#
#     if previous_x1 < MIN_INDEX or previous_y1 < MIN_INDEX:
#         print(table[x2][y2])
#         continue
#
#     print(table[x2][y2] - table[previous_x1][previous_y1])
#
#===========================================================

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * (n + 1)]
D = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
    print(result)
