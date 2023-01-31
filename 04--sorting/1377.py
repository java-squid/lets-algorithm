import sys

input = sys.stdin.readline

count = int(input())
numbers = [(int(input()), i) for i in range(count)]

max = 0
# python의 sort는 O(NlogN)의 성능을 갖는다.
sorted_numbers = sorted(numbers)
for i in range(len(sorted_numbers)):
    if sorted_numbers[i][1] - i > max:
        max = sorted_numbers[i][1] - i

# 정렬이 일어나지 않은 구간도 포함되므로 +1이 필요하다.
print(max + 1)
