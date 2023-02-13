import math
import sys

input = sys.stdin.readline


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def dfs(number, N):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:  # 2,4,6,8.. 이 자리수는 탐색이 불필요함 항상 짝수임.
                continue

            acc_num = number * 10 + i # 20 + 3 = 23
            if is_prime(acc_num):
                dfs(acc_num, N)


def solve():
    N = int(input())
    primes = [2, 3, 5, 7]

    for prime in primes:
        dfs(prime, N)


if __name__ == '__main__':
    solve()

# 문제 이해
# 각자리를 잘라가면서 소수 판별하면 되지 않을까? -> DFS 니까 재귀로 풀 수 있는 방법을 고려해봐야할듯
# 특정자리를 더해가면서 원하는 길이 N 만큼 되었을 경우 프린트하는 방법?
#

# 제한 조건
# N은 최대 8, 즉 8자리 숫자가 주어지는 것.

# 참고
# https://seongonion.tistory.com/43
