numbers = [[int(number) for number in sums.split('+')] for sums in (input().split('-'))]

sums = []
for number in numbers:
    sums.append(sum(number))

result = sums[0]
for i in range(1, len(sums)):
    result -= sums[i]

print(result)

# 마이너스 기준으로 split
# 플러스 기준으로 다시 split
# 마이너스 기준으로 split 된 숫자의 총합을 모두 마이너스 연산