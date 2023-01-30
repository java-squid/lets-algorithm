import sys

input = sys.stdin.readline().strip()


def solve():
    N = input
    arr = [int(x) for x in str(N)]

    for i in range(len(N)):
        max_index = i
        for j in range(i + 1, len(N)):
            if arr[j] > arr[max_index]:
                max_index = j
        if arr[max_index] > arr[i]:
            arr[i], arr[max_index] = arr[max_index], arr[i]

    print(*arr, sep='')


if __name__ == '__main__':
    solve()

# 문제 이해
# 선택 정렬, O(n^2), 최소값을 찾아서, 가장 앞에 있는 데이터와 스왑하는 것이 선택 정렬

# sudo code
# N
# N to arr and list(tuple(value, index)
# index = 0
# for i in range(len(list)):
#     min = min(list)
#     swap arr[0], arr[min[1]]
#     index += 1
# print(arr)