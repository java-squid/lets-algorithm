# https://www.acmicpc.net/problem/1253

import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()  # O(nlogn)
    result = 0

    for i in range(N):
        target = A[i]
        a = 0
        b = N - 1
        while a < b:
            if A[a] + A[b] > target:
                b -= 1
            elif A[a] + A[b] < target:
                a += 1
            else:
                # A[a] + A[b] == target
                if a != i and b != i: #정렬된 데이터에서 자기 자신을 포함하면 안됨.
                    result += 1
                    break
                elif a == i:
                    a += 1
                elif b == i:
                    b -= 1

    print(result)


if __name__ == '__main__':
    solve()

# sudo code
# 10, 1,2,3,4,5,6,7,8,9,10 -> 3(1,2), 4(1,3), 5(1,4,2,3) 6(1,5,2,4), 7(1,6,2,5,3,4) 8(1,7,2,6,3,5), 9(1,8,2,7,3,6,4,5), 10(1,9,2,8,3,7,4,6,)
# 4-> (2,2)는 안되나?
# 정답 8
# N 데이터 갯수
# A 데이터
#

# 제한 조건
# 수의 위치가 다르면 값이 같아도 다른 수이다. -> 같은 값이 있을 수 있음. dict 자료구조를 이용할 수는 없을듯.
