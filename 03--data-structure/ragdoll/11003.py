from collections import deque

number_count, window_size = map(int, input().split())
numbers = list(map(int, input().split()))

deq = deque()
for i in range(number_count):
    while deq and deq[-1][0] > numbers[i]:  # 덱에 존재하는 숫자보다 i 인덱스에 위치한 숫자가 작으면
        deq.pop()  # 덱에서 해당 수를 제거한다.
    deq.append((numbers[i], i))

    if deq[0][1] <= i - window_size:
        deq.popleft()

    print(deq[0][0], end=' ')
