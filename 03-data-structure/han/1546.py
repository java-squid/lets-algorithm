# https://www.acmicpc.net/problem/1546
def solve():
    n = int(input())
    scores = list(input().split())  # split default separator is any whitespace
    scores_i = [int(i) for i in scores]  # list comprehension string to int
    m = max(scores_i)  # get max number from list

    for i in range(n):  # range n (3) -> 0, 1, 2
        scores_i[i] = scores_i[i] / m * 100

    print(sum(scores_i) / n)


if __name__ == '__main__':
    solve()

# sudo code
# 1. scores (str) -> scores (int)
# 2. M = max
# 3. sum * 100 / m * 100 -> 공식

# source -> https://www.acmicpc.net/source/53787474
