# (a, b) => (a + b, c) => (a + b + c, d) => ...
# 이전 수행까지의 합을 최대한 작게 해야 비교 횟수가 작아진다.
# 데이터의 삽입, 삭제가 발생할 때 정렬을 필요로 하면 다른 컬렉션보다 우선순위 큐 사용을 고려한다.

import sys
from queue import PriorityQueue

input = sys.stdin.readline
card_count = int(input())
cards = PriorityQueue()

result = 0

for _ in range(card_count):
    cards.put(int(input()))

while cards.qsize() > 1:
    card1 = cards.get()
    card2 = cards.get()
    sum = card1 + card2
    result += sum
    cards.put(sum)

print(result)
