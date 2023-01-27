import sys
from queue import PriorityQueue

input = sys.stdin.readline


def solve():
    n = int(input())
    pq = PriorityQueue(maxsize=n)

    for i in range(n):
        p = int(input())
        if p == 0:
            if pq.empty():
                print('0')
            else:
                g = pq.get()
                print(str(g[1]))
        else:
            pq.put((abs(p), p))


if __name__ == '__main__':
    solve()

# 문제 이해
# 100,000 정도, 입력되는 정수는 마이너스 ~ 플러스
# 0이 아니려면 배열에 추가, 0이라면 배열에서 가장 작은값 출력, 그리고 그 값을 배열에서 제거
# 0일때 출력하면됨.
# 절대값이라는 단어가 왜 문제 들어가 있었을까 생각해야함.
