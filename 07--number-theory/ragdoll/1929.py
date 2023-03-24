minimum, maximum = map(int, input().split())
numbers = [True for number in range(maximum + 1)]

prime_number = True
composite_number = False
for i in range(len(numbers)):
    if i == 1:
        numbers[i] = False
        continue

    for j in range(1, len(numbers)):
        if j == 1:
            continue

        if i * j > len(numbers) - 1:
            break

        numbers[i * j] = composite_number

for i in range(minimum, maximum + 1):
    if numbers[i] is prime_number:
        print(i)
