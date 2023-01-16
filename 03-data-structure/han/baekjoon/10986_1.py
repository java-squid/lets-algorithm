# https://www.acmicpc.net/problem/11986

import sys

input = sys.stdin.readline


def solve():
    nm = list(map(int, input().split()))
    n = nm[0]
    m = nm[1]
    a = list(map(int, input().split()))
    prefix_sum = [0] * n
    remainders = [0] * m
    count = 0

    prefix_sum[0] = a[0]

    for i in range(1, n):
        prefix_sum[i] = a[i] + prefix_sum[i - 1]

    for i in range(n):
        rem = prefix_sum[i] % m
        if rem == 0:
            count += 1
        remainders[rem] += 1

    for i in range(m):
        temp = remainders[i]
        count += temp * (temp-1) // 2

    print(count)


if __name__ == '__main__':
    solve()
