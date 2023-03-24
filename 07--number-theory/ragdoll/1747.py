import math

minimum_number = int(input())
maximum_number = 10_000_000     # 오답이 나와서 범위를 이렇게 잡긴 했는데 이유를 잘 모르겠음

numbers = [0] * (maximum_number + 1)
for i in range(2, maximum_number + 1):
    numbers[i] = i

for i in range(2, int(math.sqrt(maximum_number + 1)) + 1):
    if numbers[i] == 0:
        continue

    for j in range(i + i, maximum_number + 1, i):
        numbers[j] = 0

current = minimum_number
while True:
    if numbers[current] != 0:
        split = list(str(current))
        left = 0
        right = len(split) - 1

        palindrome = True
        while left < right:
            if split[left] != split[right]:
                palindrome = False
                break

            left += 1
            right -= 1

        if palindrome:
            print(int(''.join(split)))
            break

    current += 1
