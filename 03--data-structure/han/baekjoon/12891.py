# https://www.acmicpc.net/problem/12891

import sys

input = sys.stdin.readline


def solve():
    s_length, p_length = map(int, input().split())  # dna 문자열 길이, 부분 문자열 길이
    s = input()  # DNA 문자열
    p = list(map(int, input().split()))  # A, C, G, T를 충족시켜야하는 갯수
    contain = [0] * 4
    result = 0

    def add(ch):
        if ch == 'A':
            contain[0] += 1
        elif ch == 'C':
            contain[1] += 1
        elif ch == 'G':
            contain[2] += 1
        elif ch == 'T':
            contain[3] += 1

    def remove(ch):
        if ch == 'A':
            contain[0] -= 1
        elif ch == 'C':
            contain[1] -= 1
        elif ch == 'G':
            contain[2] -= 1
        elif ch == 'T':
            contain[3] -= 1

    for i in range(p_length):
        add(s[i])

    # 슬라이딩 윈도우는 부분 문자열만 체크하는 것, 입력받은 문자열 전체가 조건에 맞춰지는지 확인해야함
    if contain[0] >= p[0] and contain[1] >= p[1] and contain[2] >= p[2] and contain[3] >= p[3]:
        result += 1

    start_index = 0
    end_index = p_length - 1

    # 슬라이딩 윈도우
    while end_index < s_length - 1:
        remove(s[start_index])
        start_index += 1
        end_index += 1
        add(s[end_index])
        if contain[0] >= p[0] and contain[1] >= p[1] and contain[2] >= p[2] and contain[3] >= p[3]:
            result += 1

    print(result)


if __name__ == '__main__':
    solve()

# 문제 이해
# DNA 문자열은 모든 문자열에 등장하는 문자가 {‘A’, ‘C’, ‘G’, ‘T’} 인 문자열
# “ACKA”는 DNA 문자열이 아니지만 “ACCA”는 DNA 문자열이다
# 부분문자열이 등장하는 위치가 다르다면 부분문자열이 같다고 하더라도 다른 문자열로 취급한다.
# 즉 ACCT와 ACTC 는 다른 문자열이라는 말인가?

# sudo code
# 문자열 별로 갯수를 세는 배열이 필요함
# 슬라이딩 윈도우 이용, 오른쪽으로 이동하면서 제거된 문자는 카운팅에서 제거하고, 추가된 문자는 카운팅에서 추가하는 방식으로

# 제한 조건
# 1 ≤ |P| ≤ |S| ≤ 1,000,000, 백만정도 들어감. 시간 복잡도가 O(N^2) 으로 들어가면 시간 초과 나지 않을까
