import sys
from collections import OrderedDict

input = sys.stdin.readline

schedule_count = int(input())

schedules = {}
for _ in range(schedule_count):
    start_time, end_time = map(int, input().split())

    if start_time not in schedules:
        schedules[start_time] = end_time
        continue

    if schedules.get(start_time) > end_time:
        schedules[start_time] = end_time

result = 0
ordered_schedules = OrderedDict(sorted(schedules.items()))
current_start_time, current_end_time = ordered_schedules.popitem(last=False)
for start_time, end_time in ordered_schedules.items():
    if start_time >= current_end_time:
        result += 1

print(result)

# Fail
# 시작시간 == 끝 시간이 같을 수 있다는 의미: 이전 회의 종료시간,
# 1. 다음 회의 시작시간이 겹칠 수 있다는 것 아니라
# 2. (2, 2)와 같은 케이스가 존재할 수 있다