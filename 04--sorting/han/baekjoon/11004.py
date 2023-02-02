import sys

input = sys.stdin.readline


def partition(arr, left, right):

    # if left + 1 == right and arr[left] > arr[right]:
    #     arr[left], arr[right] = arr[right], arr[left]
    #     return right

    # arr = 4 1 2 3 5
    # first left = 0, right = 4
    i = left # 0
    j = right - 1 # 3
    pivot = arr[right]

    while i < j:
        # i < 4 and ..
        while i < right and arr[i] < pivot:
            i += 1

        # j > 0 and..
        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


def quick_sort(arr, left, right, k):
    if left < right:
        partition_pos = partition(arr, left, right)
        # 시간 초과를 통과하기 위해서 필요한 부분만 정렬할 수 있도록 함. -> 시간 초과
        if partition_pos == k:
            return
        elif k < partition_pos:
            quick_sort(arr, left, partition_pos - 1, k)
        else:
            quick_sort(arr, partition_pos + 1, right, k)


def solve():
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))

    quick_sort(sequence, 0, len(sequence) - 1, K - 1)
    print(sequence[K - 1])


if __name__ == '__main__':
    solve()

# 문제 이해
# quick sort, 최악 O(n^2), 평균 O(nlogn)

# 제한 조건
# 1<= N,P <= 1000 -> 2중 for문 돌려도 시간 초과나진 않을듯.
# P 리스트에는 중복된 숫자가 들어가 있을 수도 있음.

# 결과
# 시간 초과

# 참고
# https://www.youtube.com/watch?v=9KBwdDEwal8
