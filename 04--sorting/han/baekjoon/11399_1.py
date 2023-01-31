import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    P = list(map(int, input().split()))

    P.sort()
    result = 0

    for i in range(1, N + 1):
        result += sum(P[0:i])

    print(result)


if __name__ == '__main__':
    solve()

# 문제 이해
# sort() 메서드 이용, slice arr..
# 소요 시간의 최솟 값. 예시를 보았을 때, 걸리는 시간 P 리스트를 오름차순으로 정렬하고 다 더하면 될듯.

# sudo code
# 입력
# P.sort()
# for i in range(1, N + 1)
#      result += sum(arr[0:i])


# 제한 조건
# 1<= N,P <= 1000 -> 2중 for문 돌려도 시간 초과나진 않을듯.
# P 리스트에는 중복된 숫자가 들어가 있을 수도 있음.

