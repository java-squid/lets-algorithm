from queue import PriorityQueue

number_count = int(input())
positive_queue = PriorityQueue()
negative_queue = PriorityQueue()

one = 0
zero = 0

for i in range(number_count):
    number = int(input())

    if number > 1:
        positive_queue.put(number * -1)
    elif number == 1:
        one += 1
    elif number == 0:
        zero += 1
    else:
        negative_queue.put(number)

sum = 0

while positive_queue.qsize() > 1:
    first = positive_queue.get() * (-1)
    second = positive_queue.get() * (-1)
    sum += first * second

if positive_queue.qsize() > 0:
    sum += positive_queue.get() * (-1)

while negative_queue.qsize() > 1:
    first = negative_queue.get()
    second = negative_queue.get()
    sum += first * second

if negative_queue.qsize() > 0:
    if zero == 0:
        sum += negative_queue.get()

sum += one
print(sum)
