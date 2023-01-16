# https://www.acmicpc.net/problem/2018
def solve():
    n = int(input())
    count = 1
    start_index = 1
    end_index = 1
    sum = 1  # 맨처음 시작하는 1은 합해졌다고 설정

    while end_index != n: # end_index == n 이면 end_index를 더 이상 증가해선 안됨. 그러면 범위를 벗어나니
        if n > sum:
            end_index += 1
            sum += end_index
        elif sum == n:
            count += 1
            end_index += 1
            sum += end_index
        else:  # n < sum
            sum -= start_index
            start_index += 1
    print(count)


if __name__ == '__main__':
    solve()

# 문제 이해
# N = 15
# 1 ~ 15 사이에 특정한 자연수를 선택해서 15가 될 수 있는 경우의 수를 찾아라
# 15만 뽑으면 될 테니.. 무조건 1번은 있을 테고
# 이게 왜 투포인터 ?
# 연속된 숫자이니까 특정 조건에 따라 start, end 포인터를 증가하여 조정하는듯. 그래서 투포인터
# 수학적인 센스가 있어야 풀듯?
