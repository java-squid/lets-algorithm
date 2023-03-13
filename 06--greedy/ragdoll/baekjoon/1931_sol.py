schedule_count = int(input())
schedules = [[0] * 2 for _ in range(schedule_count)]

for i in range(schedule_count):
    start_time, end_time = map(int, input().split())
    schedules[i][0] = end_time
    schedules[i][1] = start_time

schedules.sort()
count = 0
end_time = -1

for i in range(schedule_count):
    if schedules[i][1] >= end_time:
        end_time = schedules[i][0]
        count += 1

print(count)
