###### 시간 초과
import sys


def quick_sort(arr: list, left: int, right: int, search_index: int) -> None:
    if left < right:
        pivot = divide(arr, left, right)
        if pivot == search_index:
            return
        if pivot > search_index:
            quick_sort(arr, left, pivot - 1, search_index)
        if pivot < search_index:
            quick_sort(arr, pivot + 1, right, search_index)


def divide(arr: list, left: int, right: int) -> int:
    pivot = arr[left]
    left_start_index = left + 1
    right_start_index = right

    while left_start_index < right_start_index:
        while left_start_index < right and pivot > arr[left_start_index]:
            left_start_index += 1

        while right_start_index > (left + 1) and pivot < arr[right_start_index]:
            right_start_index -= 1

        if left_start_index < right_start_index:
            temp = arr[left_start_index]
            arr[left_start_index] = arr[right_start_index]
            arr[right_start_index] = temp

    if arr[right_start_index] < pivot:
        temp = arr[left]
        arr[left] = arr[right_start_index]
        arr[right_start_index] = temp

    return right_start_index


input = sys.stdin.readline
count, k_th = map(int, input().split())
k_index = k_th - 1

numbers = [int(number) for number in input().split()]
quick_sort(numbers, 0, len(numbers) - 1, k_index)

print(numbers[k_index])

# count, k_th = map(int, input().split())
# k_index = k_th - 1
#
# numbers = [int(number) for number in input().split()]
# numbers.sort()
#
# print(numbers[k_index])
