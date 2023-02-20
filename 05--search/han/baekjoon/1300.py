import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    k = int(input())

    start = 1
    end = k
    result = 0

    while start <= end:
        mid_index = (start + end) // 2
        cnt = 0

        for i in range(1, N + 1):
            # cnt를 더하는 이유?
            # mid 보다 작은 숫자의 합 (몇개가 있는지)
            # 이걸 생각해낼 수 있을까? ->  못할듯
            cnt += min(mid_index // i, N)

        if cnt < k:
            start = mid_index + 1
        else:
            result = mid_index
            end = mid_index - 1

    print(result)


if __name__ == '__main__':
    solve()

# 문제 이해
# arr = [0] * (N * N) 3x3 배열을 어떻게 만들까? 2차원 배열을 만들어야하나? -> 메모리 초과
# 2차원 배열을 일차원 배열로 어떻게 치환시키지? 20분 고민 못풀었음 -> 답변
# 힌트를 보니, 배열을 구현해선 안되고, k번째 수는 반드시 k 보다 작을 수 밖에 없다는 점을 이용해야할듯.


# 제한 조건
# N <= 10^5 -> 이중 for문 돌리면 안될듯

# 참고
# https://bio-info.tistory.com/207
