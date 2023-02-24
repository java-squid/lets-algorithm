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
        return

    # 자릿수는 1~9까지 나오니
    for i in range(1, 10):
        if i % 2 == 0:
            continue

        acc_num = number * 10 + i

        if is_prime(acc_num):
            dfs(acc_num, N)


def solve():
    N = int(input())

    for i in range(2, 10):
        if is_prime(i):
            dfs(i, N)


if __name__ == '__main__':
    solve()

# 문제 이해
# 어떻게 해야할지 감이 안옴. -> sad..
# 답안 보고 다시 분석해보자

# sudo code
# 1. 우선 소수 판단에 대한 함수가 필요할듯. 소수는 1보다 큰 자연수 중에 자기 자신을 제외한 자연수로 나누어떨어지지 않는 자연수
# 2. dfs 를 이용해 특정 자리 수 이상이 되면 리턴하도록. 아니면 자리수를 더해 재귀되도록

# 제한 조건
