lesson_count, blue_ray_count = map(int, input().split())
minutes = [int(minute) for minute in input().split()]

result = 0

# 최대 최소를 정하고 답의 범위를 좁혀나간다.
minimum = max(minutes)
maximum = sum(minutes)

while minimum <= maximum:
    middle = (minimum + maximum) // 2

    count = 1
    sum = 0

    for minute in minutes:
        if sum + minute > middle:
            count += 1
            sum = minute
        else:
            sum += minute

    if count <= blue_ray_count:
        result = middle
        maximum = middle - 1
    else:
        minimum = middle + 1

print(result)
