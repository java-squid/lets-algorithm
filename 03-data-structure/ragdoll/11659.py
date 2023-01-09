counts = input()
numbers = [int(number) for number in input().split()]
start, end = [int(range) - 1 for range in input().split()]

interval_sum = []
sum = 0
for number in numbers:
    sum += number
    interval_sum.append(sum)

print(interval_sum)

print(interval_sum[end] - interval_sum[start - 1])
