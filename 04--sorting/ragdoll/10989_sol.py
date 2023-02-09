import sys
input = sys.stdin.readline

n = int(input())
counts = [0] * 10_001

for i in range(n):
    counts[int(input())] += 1

for i in range(10_001):
    if counts[i] != 0:
        for _ in range(counts[i]):
            print(i)