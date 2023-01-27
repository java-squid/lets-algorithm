# https://www.acmicpc.net/problem/11720
def solve():
    n = int(input())
    numbers = list(input())
    sum = 0

    for i in range(n):
        sum += int(numbers[i])

    print(sum)


if __name__ == '__main__':
    solve()

# source -> https://www.acmicpc.net/source/53786387
