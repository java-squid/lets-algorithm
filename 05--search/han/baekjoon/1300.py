import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    k = int(input())

    start = 1
    end = k
    result = 0

    while start <= end:
        mid = (start + end) // 2

        # 중앙값 mid 보다 작거나 같은 수의 갯수
        count_of_less_than_equal_mid = sum(min(mid // i, N) for i in range(1, N + 1))

        # 만약에 mid 보다 작은 값들의 갯수 k보다 작다면, 시작 인덱스를 mid + 1로 옮김.
        # mid + 1 이후 부터 다시 계산해서 k보다 크거나 같은 값이 나오도록.
        if count_of_less_than_equal_mid < k:
            start = mid + 1
        else:
            result = mid
            end = mid - 1

    print(result)


if __name__ == '__main__':
    solve()

# 문제 이해
# arr = [0] * (N * N) 3x3 배열을 어떻게 만들까? 2차원 배열을 만들어야하나? -> 메모리 초과
# 2차원 배열을 일차원 배열로 어떻게 치환시키지? 20분 고민 못풀었음 -> 답변
# 힌트를 보니, 배열을 구현해선 안되고, k번째 수는 반드시 k 보다 작을 수 밖에 없다는 점을 이용해야할듯.
# 아직까지 인덱스 값(mid)을 리턴했는데 어떻게 오름차순으로 정렬된 B[k] 가 되는지 이해 안됨

# 제한 조건
# N <= 10^5 -> 이중 for문 돌리면 안될듯

# 참고
# https://bio-info.tistory.com/207
