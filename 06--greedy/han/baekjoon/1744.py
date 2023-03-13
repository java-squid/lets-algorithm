from queue import PriorityQueue
import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    plus_pq = PriorityQueue()
    minus_pq = PriorityQueue()
    count_one = 0
    count_zero = 0

    for _ in range(N):
        temp = int(input())
        if temp == 0:
            count_zero += 1
        elif temp == 1:
            count_one += 1
        elif temp > 1:
            plus_pq.put(temp * -1) # 내림차순 정렬을 위해서
        else:
            minus_pq.put(temp)

    result = 0

    while plus_pq.qsize() > 1:
        a = plus_pq.get()
        b = plus_pq.get()
        result += a * b

    if plus_pq.qsize() > 0:
        result += plus_pq.get() * -1

    while minus_pq.qsize() > 1:
        a = minus_pq.get()
        b = minus_pq.get()
        result += a * b

    if minus_pq.qsize() > 0 and count_zero > 0:
        minus_pq.get()
        count_zero -= 1

    if minus_pq.qsize() > 0:
        result += minus_pq.get()

    if count_one > 0:
        result += count_one

    print(result)


if __name__ == '__main__':
    solve()

# 문제 이해
# 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능하다.  -> 같은 인덱스에 있는 값을 두번 선택할 순 없음.
# 어떤 수를 묶게 되면, 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다. -> 마이너스와 플러스 수를 묶으면 안될듯
# 양수, 음수로 나눠서 큐를 관리하면 될듯
# 그 값이 최대가 되어야함
# Priority queue 를 이용

# 시간초과.. -> 오타 ㅎㅎ
