import sys

input = sys.stdin.readline
count = int(input())

for i in range(count):
    number1, number2 = map(int, input().split())

    big_number = max(number1, number2)
    small_number = min(number1, number2)

    if big_number % small_number == 0:
        print(big_number)
        continue

    while small_number != 0:
        mod = big_number % small_number
        big_number = small_number
        small_number = mod

    the_greatest_common_divisor = big_number

    print((number1 * number2) // the_greatest_common_divisor)
