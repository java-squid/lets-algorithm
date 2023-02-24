import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    M = list(map(int, input().split()))

    dict = {i: 1 for i in A}

    for m in M:
        if m in dict:
            print("1", end='\n')
        else:
            print("0", end='\n')


if __name__ == '__main__':
    solve()

# 문제 이해
# 어떤 리스트의 값이 다른 리스트에 있는지 확인만 하면 되니까, 딕셔너리 자료구조를 이용하면 되지 않을까?

# 제한 조건
# 1 <= N <= 100,000

# 참고
# https://seongonion.tistory.com/43
