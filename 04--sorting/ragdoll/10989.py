#=================== 메모리 초과
import sys
from collections import deque

max_number = 10_000
input = sys.stdin.readline

count = int(input())
numbers = []
for i in range(count):
    numbers.append(int(input()))

queues = dict()
for i in range(10):
    queues[i] = deque()

for i in range(len(str(max_number))):
    for number in numbers:
        if len(str(number)) < i + 1:
            queues[0].append(number)    # i = 0 => -1, i = 1 => -2, i = 2 => -3, i = 3 => -4
        else:
            queues[int(str(number)[-i - 1])].append(number)

    numbers = []
    for j in range(0, 10):
        while len(queues[j]) > 0:
            numbers.append(queues[j].popleft())

for number in numbers:
    print(number)
