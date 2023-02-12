import sys

input = sys.stdin.readline
result = 0


def merge_sort(arr):
    # len(arr) = 1 인 경우, 정렬할 필요 없음.
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        left_arr = merge_sort(arr[:middle])
        right_arr = merge_sort(arr[middle:])
        return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    global result

    i = 0  # left arr index
    j = 0  # right arr index
    temp = []  # space complexity O(N)

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] > right_arr[j]:
            temp.append(right_arr[j])
            # left arr의 남아있는 데이터 - 현재 왼쪽에서 가리키고 있는 인덱스
            result += len(left_arr) - i
            j += 1
        else:
            temp.append(left_arr[i])
            i += 1

    while i < len(left_arr):
        temp.append(left_arr[i])
        i += 1

    while j < len(right_arr):
        temp.append(right_arr[j])
        j += 1

    return temp


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    sorted_arr = merge_sort(A)
    print(sorted_arr)
    print(result)


if __name__ == '__main__':
    solve()

# 문제 이해
# 버블 정렬을 이용할 때 몇번의 swap 이 일어나는지
# 1 ≤ N ≤ 500,000 -> 버블정렬 시간복잡도가 O(N^2)이어서 버블정렬을 이용할 경우 1초 내에 풀 수 없을듯.
# 병합정렬을 이용해보면..?
# 정렬 진행 할 때 인덱스를 알아야하는듯.

# 반례
# Input
# 2
# 1 1

# 참고
# https://goodsosbva.tistory.com/45?category=454008
