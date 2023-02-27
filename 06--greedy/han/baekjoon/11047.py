import sys

input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    coin = [0] * N

    for i in range(N):
        coin[i] = int(input())

    count = 0
    for i in range(N - 1, -1, -1):
        if coin[i] <= K:
            count += int(K // coin[i])
            K = K % coin[i]

    print(count)


if __name__ == '__main__':
    solve()

# 문제 이해
# 나오는 코인의 종류의 수는 최대 10개., 코인의 갯수는 무한정 있음. 즉 1원짜리 무한정 사용 가능.
# 10분 고민, 못풀것 같음. 최소값을 어떻게 알 수 있지?
# 최소 갯수를 파악하라면, 가장 큰 값부터 몇개 쓸지 카운팅을 해야 전반적으로 숫자가 가장 작아질 수 있음

# 제한 조건
# 1 ≤ N ≤ 10, 코인 종료 쵀대 10개

