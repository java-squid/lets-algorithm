import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    arr = [0] * n

    stk = []
    num = 1
    result = ""

    for i in range(n):
        # 4 3 6 8 7 5 2 1
        # 1 2 5 3 4
        # 1 2 5 6 4
        arr[i] = int(input())

    for i in range(n):
        target = arr[i]
        if target >= num:
            while target >= num:
                stk.append(num)
                num += 1
                result += '+\n'
            stk.pop()
            result += '-\n'
        else:  # target < num
            last_num = stk.pop()
            if last_num > target:
                # 왜? 문제 조건 인것 같은데.. 이해 안됨 4(last_num) > 3(target), num(5) num을 append할 수도 없고 증가하기만
                # 해야하니. 성립하는 수열이라면 이 부분에서 반드시 last_num <= target이어야 하는듯
                result = 'NO'
                break
            else:
                result += '-\n'

    print(result)


if __name__ == '__main__':
    solve()

# 문제 이해
# 자연수는 증가하기만 해야하고,

# 제한 조건
# 1 ≤ n ≤ 100,000, 그리 크지 않은 범위 인듯, 1부터 시작
# 스택에 push하는 순서는 반드시 오름차순을 지킴
