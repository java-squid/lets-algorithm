import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    M = list(map(int, input().split()))

    # sort asc
    A.sort()

    for target in M:
        result = 0

        start_index = 0
        end_index = len(A) - 1

        while start_index <= end_index:
            mid = (start_index + end_index) // 2

            if A[mid] > target:
                end_index = mid - 1
            elif A[mid] < target:
                start_index = mid + 1
            else:
                result = 1
                break

        print(result, end='\n')


if __name__ == '__main__':
    solve()

# 문제 이해
# 이진 검색 알고리즘을 사용해서 풀어보자
# arr slicing 으로 푸는 방법 -> 시간 초과
# index를 재설정해서 푸는 방법 -> 통과

# 제한 조건
# 1 <= N <= 100,000

# 참고
# https://seongonion.tistory.com/43
