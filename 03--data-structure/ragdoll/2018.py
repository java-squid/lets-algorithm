# ==================================================
# target_number = int(input())
# numbers = list(range(1, (target_number // 2) + 2))
#
# result = 1
# left = 0
# right = left + 1
# sum = numbers[left]
# while right <= len(numbers) - 1:
#     sum += numbers[right]
#     right += 1
#     if sum == target_number:
#         result += 1
#
#     while sum >= target_number:
#         sum -= numbers[left]
#         left += 1
#         if sum == target_number:
#             result += 1
#
# print(result)
# ==================================================
#
# target_number = int(input())
#
# result = 1
# left = 1
# right = left + 1
# sum = left
# while right < target_number:
#     sum += right
#     right += 1
#     if sum == target_number:
#         result += 1
#
#     while sum >= target_number:
#         sum -= left
#         left += 1
#         if sum == target_number:
#             result += 1
#
# print(result)
# ==================================================
n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(count)
