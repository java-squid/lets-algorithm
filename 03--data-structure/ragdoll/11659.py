# ============================================================================
# 시간 초과 발생
#
# number_count, calculation_count = [int(count) for count in input().split()]
# numbers = [int(number) for number in input().split()]
#
# interval_sum = [0]
# sum = 0
# for number in numbers:
#     sum += number
#     interval_sum.append(sum)
#
# for index in range(calculation_count):
#     start, end = [int(interval) for interval in input().split()]
#     print(interval_sum[end] - interval_sum[start - 1])
# ============================================================================
import sys

input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])
