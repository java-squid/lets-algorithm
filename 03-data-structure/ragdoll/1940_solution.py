import sys

input = sys.stdin.readline

n = int(input())  # 재료 수
m = int(input())  # 갑옷이 되는 번호
a = list(map(int, input().split()))  # 재료 저장 리스트
a.sort()
count = 0  # 정답 수
i = 0  # start
j = n - 1  # end

while i < j:
    if a[i] + a[j] < m:
        i += 1
    elif a[i] + a[j] > m:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)
