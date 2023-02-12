import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    A = [0] * 10001

    for _ in range(N):
        num = int(input())
        A[num] += 1

    for i in range(10001):
        if A[i] is 0:
            continue

        for _ in range(A[i]):
            print(i)


if __name__ == '__main__':
    solve()

# 문제 이해
# counting sort ?
# N 만큼 배열 만들고, 카운팅 해서 1 이상인 것들을 그 인덱스만큼 출력하면 되지 않을까?
# N(1 ≤ N ≤ 10,000,000) -> 굉장히 큰 숫자. 5초..안에 하려면 O(N) 이나 그 미만 O(nlogn)은 안된다??
