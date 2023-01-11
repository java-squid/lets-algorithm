# https://www.acmicpc.net/problem/11986

import sys

input = sys.stdin.readline


def solve():
    nm = list(input().split())
    n = int(nm[0])  # 5
    m = int(nm[1])  # 3
    A = list(map(int, input().split()))  # 1 2 3 1 2
    S = [0] * n  # 합배열 0, 0, 0, 0, 0
    C = [0] * m
    S[0] = A[0]
    res = 0

    # 합배열 저장
    for i in range(1, n):
        S[i] = S[i - 1] + A[i]

    # M으로 나눠지는 수 찾기
    for i in range(n):
        rem = S[i] % m
        if rem == 0:
            res += 1
        C[rem] += 1

    for i in range(m):
        if C[i] > 1:  # 나머지가 같은 인덱스가 2개 이상 있음.
            # 공식 NC2 = n * (n-1) / 2 -> C[i] * (C[i] - 1) / 2,
            res += C[i] * (C[i] - 1) // 2

    print(res)


if __name__ == '__main__':
    solve()

# 문제 이해
# 잘 안됨,
# (A + B) % C = ((A % C) + (B % C)) % C 핵심
