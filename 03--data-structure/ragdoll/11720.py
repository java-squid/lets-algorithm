count_of_numbers = input()
numbers = map(int, input())

total = 0
for number in numbers:
    total += number

print(total)