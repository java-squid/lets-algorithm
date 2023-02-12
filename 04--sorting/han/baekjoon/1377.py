import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    A = []

    for i in range(N):
        A.append((int(input()), i))  # 정렬 전 인덱스

    sorted_A = sorted(A)

    result = 0

    for i in range(N):
        index_beforeSorted = sorted_A[i][1]
        index_afterSorted = i
        result = max(result, index_beforeSorted - index_afterSorted)

    print(result + 1)


if __name__ == '__main__':
    solve()

# 문제 이해
# N은 배열의 크기, A는 정렬해야하는 배열, 배열은 A[1] 부터 시작함.
# 예제에서 왜 3이 출력되는지 이해 안됨  -> 해답 참조 -> swap이 한번도 일어나지 않는 바깥 루프 i 값을 출력하는듯.
# 기존 인덱스, 정렬된 인덱스를 기반으로 비교..?
# 2번째 루프에서 완벽하게 정렬이 되었어도, 3번째도 루프도 실행되긴 함.

# 제한 조건
# N 쵀대 500,000, 버블 소트로 풀면 500,000 ^ 2로 시간내 못풀 것 같음.

# 참고
# https://steady-coding.tistory.com/41