import sys

def merge_sort(arr: list, left: int, right: int) -> None:
    if left < right:
        middle = (left + right) // 2
        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)
        merge(arr, left, middle, right)


def merge(arr: list, left: int, middle: int, right: int) -> None:
    global move_count
    left_area_index = left
    right_area_index = middle + 1
    merge_array_index = left

    while left_area_index <= middle and right_area_index <= right:
        if arr[left_area_index] <= arr[right_area_index]:
            merge_array[merge_array_index] = arr[left_area_index]
            left_area_index += 1
        elif arr[left_area_index] > arr[right_area_index]:
            merge_array[merge_array_index] = arr[right_area_index]
            move_count = move_count + (right_area_index - merge_array_index)
            right_area_index += 1

        merge_array_index += 1

    while left_area_index <= middle:
        merge_array[merge_array_index] = arr[left_area_index]
        left_area_index += 1
        merge_array_index += 1

    while right_area_index <= right:
        merge_array[merge_array_index] = arr[right_area_index]
        right_area_index += 1
        merge_array_index += 1

    for i in range(left, right + 1):
        arr[i] = merge_array[i]


input = sys.stdin.readline

count = int(input())
numbers = list(map(int, input().split()))

move_count = 0
merge_array = [0] * count
merge_sort(numbers, 0, len(numbers) - 1)

print(move_count)
