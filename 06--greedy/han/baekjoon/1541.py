import sys

input = sys.stdin.readline


def solve():
    formula = input().strip()
    arr = formula.split('-')

    # 예제 2번 +만 있는 경우
    if len(arr) == 1:
        list_of_string = formula.split('+')
        list_of_int = [int(x) for x in list_of_string]
        print(sum(list_of_int))
    else:
        # [1+2,3+4]
        accumulate = 0

        for i in range(len(arr)):
            list_of_string = arr[i].split('+')
            list_of_int = [int(x) for x in list_of_string]

            if i == 0:
                accumulate += int(sum(list_of_int))
            else:
                accumulate -= int(sum(list_of_int))

        print(accumulate)


if __name__ == '__main__':
    solve()

# 문제 이해
# 최소값을 만들기 위해서는.. 어떤 수에 가장 큰 수를 뺴야함.
# 수식은 +,- 만 있음.
# 예제 1 -> 55 - (55 + 40) = -35
# 에제 2 -> + 만 있으므로.. 그냥 다 하는게 최소값
# 예제 3 -> 0으로 시작하는 수... 이건 어떻게 핸들링해야할까
# -> 런타임 에러 (ValueError) 발생 예제 3번 때문에 그런것 같은데 모르겠음
# -> 반례 1+2-3+4

# 수도코드
# 일단 - 로 split 해볼까?
# +만 있는 경우도 있겠다, 혹은 - 만 있는 경우도.
