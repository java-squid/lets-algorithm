number_count = int(input())

numbers = list(map(int, input().split()))

answers = [0] * number_count
stack = []
for i in range(number_count):
    while stack and numbers[stack[-1]] < numbers[i]:    # 큰 수를 찾으면 stack에서 pop, 정답 배열에 push한다.
        answers[stack.pop()] = numbers[i]
    stack.append(i)         # 큰 수가 존재하지 않는 인덱스는 남겨둔다.

while stack:
    answers[stack.pop()] = -1

for answer in answers:
    print(answer, end=' ')
