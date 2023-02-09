count = int(input())
minutes = list(map(int, input().split()))

for i in range(1, len(minutes)):
    current = minutes[i]
    insertionIndex = i

    for j in range(i - 1, -1, -1):
        if minutes[j] > current:
            minutes[j + 1] = minutes[j]
            insertionIndex = j

        if (minutes[j] <= current):
            break

    minutes[insertionIndex] = current

sum_array = [0] * len(minutes)
sum_array[0] = minutes[0]
total = sum_array[0]
for i in range(1, len(minutes)):
    sum_array[i] = sum_array[i - 1] + minutes[i]
    total += sum_array[i]

print(total)