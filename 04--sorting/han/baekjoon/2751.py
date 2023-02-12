import sys

input = sys.stdin.readline


def merge_sort(arr):
    # len(arr) = 1 인 경우, 정렬할 필요 없음.
    if len(arr) <= 1:
        return

    left_arr = arr[:len(arr) // 2]
    right_arr = arr[len(arr) // 2:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    i = 0  # left arr index
    j = 0  # right arr index
    k = 0  # merge arr index

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


def solve():
    N = int(input())
    arr = [0] * N

    # input
    for i in range(N):
        arr[i] = int(input())

    # merge sort
    merge_sort(arr)

    # print
    for i in range(N):
        print(arr[i])


if __name__ == '__main__':
    solve()

# 문제 이해
# 병합정렬 이용, Divde and Conquer, 시간복잡도 O(nlogn), recursive 이용


# 제한 조건
# 1<= N,P <=  1,000,000 -> 2중 for문 돌려도 시간 초과날듯함.

# 참고
# https://www.youtube.com/watch?v=cVZMah9kEjI
