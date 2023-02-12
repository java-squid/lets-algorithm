import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    P = list(map(int, input().split()))
    A = [0] * N

    # selection sort
    for i in range(N):
        ind = i
        for j in range(ind + 1, N):
            if P[ind] > P[j]:
                ind = j
        P[i], P[ind] = P[ind], P[i]

    # 합 배열로 변경해야함
    A[0] = P[0]
    for i in range(1, N):
        A[i] = A[i - 1] + P[i]

    print(sum(A))


if __name__ == '__main__':
    solve()

# 문제 이해
# 삽입 정렬 이용, O(N^2), asc 가정할 때, 가장 작은 걸 찾아서 맨 앞으로 swap
# O(N^2) 으로 이중 for문 이용할듯.
# 소요 시간의 최솟 값. 예시를 보았을 때, 걸리는 시간 P 리스트를 오름차순으로 정렬하고 다 더하면 될듯.


# 제한 조건
# 1<= N,P <= 1000 -> 2중 for문 돌려도 시간 초과나진 않을듯.
# P 리스트에는 중복된 숫자가 들어가 있을 수도 있음.

# 참고
# https://www.geeksforgeeks.org/python-program-for-selection-sort/
# https://www.google.com/search?q=python+selection+sort&tbm=vid&sa=X&ved=2ahUKEwi75_TU9vH8AhUK4GEKHWcPAosQ0pQJegQIDBAB&biw=1080&bih=1788&dpr=1#fpstate=ive&vld=cid:34f4dc16,vid:mI3KgJy_d7Y
