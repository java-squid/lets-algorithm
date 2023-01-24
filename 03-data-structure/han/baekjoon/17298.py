
import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    res = [-1] * n
    a = list(map(int, input().split()))
    stk = []

    for i in range(n):
        while stk and a[stk[-1]] < a[i]:
            res[stk.pop()] = a[i]
        stk.append(i)

    # 시간 초과로 아래 코드 실패
    # result = ''
    # for i in range(n):
    #     result += str(res[i]) + ' '
    #
    # print(result)
    for r in res:
        print(r, end=' ')


if __name__ == '__main__':
    solve()

# 문제 분석
# n의 크기가 백만까지 갈 수 있음. 정렬이나 반복문 통해서는 시간 제한에 걸릴 수도.
# 오큰수, 특정 인덱스 보다 오른쪽에 있으면서 큰 수중에 제일 왼쪽에 있는 것
# stack 을 이용할 거라는 필요성을 느꼈는가? -> NO

