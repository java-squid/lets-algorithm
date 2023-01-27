from collections import deque


def solve():
    n = int(input())
    dq = deque()

    for i in range(1, n + 1):
        dq.append(i)

    while len(dq) > 1:
        dq.popleft()
        dq.append(dq.popleft())

    print(dq[0])


if __name__ == '__main__':
    solve()

# 문제 분석
# 1번 카드가 제일 위헤, N번 카드게 제일 아래... -> deque이용하면 안될까?