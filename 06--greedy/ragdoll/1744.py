# 수열의 크기 : n,  0 < n <= 50
# 수열의 수 : x,  -1000 <= x <= 1000
# 1. 정렬 이후 뒷 인덱스부터 곱하기
# 2. 0은 곱셈 대상에서 제외
# 3. (-m) * (-n) 가능

number_count = int(input())
negative_numbers = []
zero_numbers = []
positive_numbers = []

for _ in range(number_count):
    number = int(input())
    if number > 0:
        positive_numbers.append(number)
    if number < 0:
        negative_numbers.append(number)
    if number == 0:
        zero_numbers.append(number)

negative_numbers.sort(reverse=True)
positive_numbers.sort()

result = 0
rest_positive_number = 0
while positive_numbers:
    temp = []
    while positive_numbers and len(temp) < 2:
        temp.append(positive_numbers.pop())

    if len(temp) == 2:
        number1 = temp.pop()
        number2 = temp.pop()
        result += (number1 * number2)
    elif len(temp) == 1:
        rest_positive_number = temp.pop()
        break

rest_negative_number = 0
while negative_numbers:
    temp = []
    while negative_numbers and len(temp) < 2:
        temp.append(negative_numbers.pop())

    if len(temp) == 2:
        number1 = temp.pop()
        number2 = temp.pop()
        result += (number1 * number2)
    elif len(temp) == 1:
        rest_negative_number = temp.pop()
        break

if not zero_numbers:
    result += (rest_positive_number + rest_negative_number)

if len(zero_numbers) >= 1:
    result += rest_positive_number
    result += (rest_negative_number * 0)

print(result)

# 반례를 못찾음