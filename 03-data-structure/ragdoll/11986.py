number_count, divide_number = map(int, input().split())
number_list = [int(x) for x in input().split()]

sum_list = [0] * number_count
answer_indexes = [0] * divide_number
sum_list[0] = number_list[0]
for i in range(1, number_count):
    sum_list[i] = sum_list[i - 1] + number_list[i]

answer = 0
for i in range(number_count):
    remainder = sum_list[i] % divide_number

    if remainder == 0:
        answer += 1

    answer_indexes[remainder] += 1

for i in range(divide_number):
    if answer_indexes[i] > 1:
        answer += (answer_indexes[i] * (answer_indexes[i] - 1) // 2)

print(answer)
