from queue import PriorityQueue


def solve():
    N = int(input())
    pq = PriorityQueue()

    for _ in range(N):
        temp = int(input())
        pq.put(temp)

    result = 0

    while pq.qsize() > 1:
        a = pq.get()
        b = pq.get()
        sum_a_and_b = a + b
        result += sum_a_and_b
        pq.put(sum_a_and_b)

    print(result)


if __name__ == '__main__':
    solve()

# 문제 이해
# 카드 묶음을 가장 최소한으로 비교하기 위해선?
# 가장 작은 것 2개를 묶어서 다시 넣어야할듯

# 피드백
# 시간초과 ? pypy3는 시간초과 나는듯 이유는 모르겠음
