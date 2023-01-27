import sys

count = int(input())
numbers = [int(input()) for _ in range(count)]

stack = []
answers = []
current = 1

for i in range(count):
    target = numbers[i]

    if target >= current:
        while target >= current:
            stack.append(current)
            current += 1
            answers.append('+')

        stack.pop()
        answers.append('-')
    else:
        number = stack.pop()

        if number != target:
            answers = ['NO']
            break

        answers.append('-')

for answer in answers:
    print(answer)
