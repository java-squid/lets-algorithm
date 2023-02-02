import sys

input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))
    sequence.sort()
    print(sequence[K - 1])


if __name__ == '__main__':
    solve()

# 문제 이해
# sort 이용하면 될듯.

# 제한 조건
# N(1 ≤ N ≤ 5,000,000) -> O(N^2) 일 경우 시간 초과 날듯.
