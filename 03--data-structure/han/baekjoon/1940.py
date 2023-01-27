# https://www.acmicpc.net/problem/1940
def solve():
    n = int(input())
    m = int(input())
    temp = list(map(int, input().split()))
    ingredients = {}
    count = 0

    for i in range(n):
        ingredients[temp[i]] = 0

    # 2 7 4 1 5 3
    for i in range(n):
        target = m - temp[i] # 9 - 2 = 7
        if target in ingredients and ingredients[target] != 1 and target != temp[i]:
            count += 1
            ingredients[temp[i]] += 1

    print(count)


if __name__ == '__main__':
    solve()

# dict 사용
# 고유한 값이라는 것에 주목 m = 4 2,2 이렇게 달성될 순 없음
# 추가 확인 케이스 (and target != temp[i] 이 조건 있어야 통과함
# 3
# 4
# 1 2 3