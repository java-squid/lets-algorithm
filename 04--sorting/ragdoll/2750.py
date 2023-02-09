count = int(input())

numbers = []
for _ in range(count):
    numbers.append(int(input()))

for i in range(0, len(numbers) - 1):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

for number in numbers:
    print(number)

