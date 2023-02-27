# 문제 조건에 의해 주어지는 동전은 오름차순 정렬
# => 동전의 최소 개수를 구하는 것이기 때문에 가장 큰 동전부터 탐색 (마지막 인덱스부터)

import sys

input = sys.stdin.readline

coin_count, target = map(int, input().split())

coins = [int(input()) for _ in range(coin_count)]

result = 0

for i in range(coin_count - 1, -1, -1):
    if coins[i] <= target:
        result += target // coins[i]
        target %= coins[i]

print(result)
