# https://www.acmicpc.net/problem/1940
def solve():
    n = int(input())
    m = int(input())
    a = list(map(int, input().split()))
    count = 0
    a.sort()
    i = 0
    j = n - 1

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


if __name__ == '__main__':
    solve()

# 투 포인터
