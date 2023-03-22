import math
import sys

input = sys.stdin.readline


def solve():
    M, N = map(int, input().split())

    arr = [i for i in range(N + 1)]

    # 1은 소수가 아니니, 인덱스 2부터 시작
    for i in range(2, int(math.sqrt(N) + 1)):
        if arr[i] == -1:
            continue

        for j in range(i + i, N + 1, i):
            arr[j] = -1

    for i in range(2, len(arr)):
        if arr[i] != -1 and arr[i] >= M:
            print(arr[i], end='\n')


if __name__ == '__main__':
    solve()

# 문제 이해

# 수도코드
# 에라토스테네스의 체 그대로 구현 -> 시간 초과
# 시간 초과는 효율화가 안된거.. 내가 뭐 놓친 거 있나? -> N의 제곱근 까지만 탐색한다
# 배수 판단은 range 파라미터의 마지막에서 판단..
