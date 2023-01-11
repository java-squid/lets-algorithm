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