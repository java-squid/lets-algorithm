from queue import PriorityQueue
import sys

print = sys.stdout.write
input = sys.stdin.readline
count = int(input())
queue = PriorityQueue()

for i in range(count):
    number = int(input())
    if number == 0:
        if queue.empty():
            print('0\n')
        else:
            temp = queue.get()
            print(str((temp[1])) + '\n')
    else:
        queue.put((abs(number), number))
