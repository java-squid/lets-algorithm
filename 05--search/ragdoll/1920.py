import sys

input = sys.stdin.readline

n_count = int(input())
n_numbers = list(map(int, input().split()))

n_numbers.sort()

m_count = int(input())
m_numbers = list(map(int, input().split()))


def binary_search(search_target: int, start: int, end: int) -> int:
    if start > end:
        return 0

    middle = (start + end) // 2
    if n_numbers[middle] == search_target:
        return 1
    if n_numbers[middle] > search_target:
        return binary_search(search_target, start, middle - 1)
    if n_numbers[middle] < search_target:
        return binary_search(search_target, middle + 1, end)


for number in m_numbers:
    search = binary_search(number, 0, n_count - 1)
    print(search)
