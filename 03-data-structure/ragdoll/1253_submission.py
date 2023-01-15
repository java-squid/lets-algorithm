# Fail
number_count = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

good_numbers = set()
left = 0
right = left + 1

last_index = len(numbers) - 1
max_number = numbers[last_index]

while right <= last_index:
    sum = numbers[left] + numbers[right]

    if numbers.__contains__(sum) and numbers[left] != 0 and numbers[right] != 0:
        good_numbers.add(sum)

    if sum < max_number:
        right += 1

    if sum >= max_number:
        left += 1
        right = left + 1

print(len(good_numbers))
