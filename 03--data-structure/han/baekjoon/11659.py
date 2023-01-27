# https://www.acmicpc.net/problem/11659
# https://www.acmicpc.net/source/53851784
# https://www.acmicpc.net/source/53852969


import sys

input = sys.stdin.readline


# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
# 반복문으로 여러 입력을 받는 상황에서는 시간초과를 방지하기 위해 사용해야하는듯.

def solve_1():
    nm = list(input().split())
    n = int(nm[0])
    m = int(nm[1])

    a = list(input().split())
    s = []
    result = []

    for i in range(n):
        if i == 0:
            s.append(int(a[0]))
            continue
        # S[i] = S[i-1] + A[i]
        s.append(int(a[i]) + int(s[i - 1]))

    for i in range(m):
        temp = list(input().split())
        a = s[int(temp[1]) - 1]
        b = 0 if int(temp[0]) - 1 == 0 else s[int(temp[0]) - 2]
        result.append(a - b)

    for i in result:
        print(i)


def solve_2():
    nm = list(input().split())
    n = int(nm[0])
    m = int(nm[1])

    a = list(input().split())
    s = [0]
    temp = 0

    for i in range(n):
        temp += int(a[i])
        s.append(temp)

    for i in range(m):
        key, value = map(int, input().split())
        print(s[value] - s[key - 1])


if __name__ == '__main__':
    # solve_1()
    solve_2()

# 풀이
# 5 3 n = 5, m = 3, n은 2번째 요소의 갯수, m은 구간합을 인덱스 의 갯수 (1,3 | 2,4 | 5,5)
# n, m 의 경우 100,000까지 가능 -> 100,000 * 100,000 = 1,000,000,000,000
# 합배열 이용
