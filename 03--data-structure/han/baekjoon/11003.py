# https://www.acmicpc.net/problem/12891

import sys
from collections import deque
input = sys.stdin.readline


def solve():
    n, l = map(int, input().split())  # n = 숫자의 갯수, l 슬라이딩 윈도우의 크기
    numbers = list(map(int, input().split()))
    dq = deque()

    for i in range(n):
        # 맨 뒤에 있는 노드의 value가, numbers[i] 보다 크다면 pop() 되어야함. 항상 맨 처음 노드엔 최소값만 남도록..
        while dq and dq[-1][1] > numbers[i]:
            dq.pop()
        dq.append((i, numbers[i])) # index, value
        if dq and dq[0][0] < i - l + 1:
            dq.popleft()

        print(dq[0][1], end=' ')


if __name__ == '__main__':
    solve()

# 문제 이해
# 일정 범위 안에서 최소값을 구하는 것 -> 슬라이딩 윈도우
# 출력은 n 개 만큼 나올듯.
# l = 3 이면, A(i-4) ~ A(i) = D(i)
# i = 0, A(-4) ~ A(0) = D(0)
# 이때 i <= 0인 A(i)는 무시한다. -> 인덱스가 l 범위를 벗어났다면 무시한다. (popleft한다)

# sudo code



# 제한사항

# 기타
# deque말고 다른 방법은 없을까?