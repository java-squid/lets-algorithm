import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    arr = []

    for _ in range(N):
        arr.append(int(input()))

    for i in range(N - 1):
        for j in range(N - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    for a in arr:
        print(a)


if __name__ == '__main__':
    solve()

# sudo code
# swap을 이용
# n = 5
# list = []
# for _ in ragne(n)
#   list.append(int(input))
# bubble sort
# print(list)


# 제한 조건
# 주어지는 수는 중복되지 않음.
# 버블 정렬을 통해 구현하고 풀어볼 것

# 기타
# 버블소트는 시간복잡도 O(n^2)