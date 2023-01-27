from collections import deque

count = int(input())

numbers = deque()
for i in range(1, count + 1):
    numbers.appendleft(i)

while len(numbers) > 1:
    numbers.pop()
    number = numbers.pop()
    numbers.appendleft(number)

for number in numbers:
    print(number)
