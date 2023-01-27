# =========================================================================
# Fail
#
# class SubMission:
#
#     def main(self):
#         dna_length, password_length = map(int, input().split())
#         dna = list(input())
#         A_COUNT, C_COUNT, G_COUNT, T_COUNT = map(int, input().split())
#
#         minimum_counts = dict(
#             A=A_COUNT,
#             C=C_COUNT,
#             G=G_COUNT,
#             T=T_COUNT
#         )
#
#         counts = dict(
#             A=0,
#             C=0,
#             G=0,
#             T=0
#         )
#
#         def is_valid_password() -> bool:
#             for key, value in counts.items():
#                 if value < minimum_counts.get(key):
#                     return False
#
#             return True
#
#         answer = 0
#         left = 0
#         right = left + (password_length - 1)
#         for i in range(left, right + 1):
#             counts[dna[i]] = counts.get(dna[i]) + 1
#
#         if is_valid_password():
#             answer += 1
#
#         counts[dna[left]] = counts.get(dna[left]) - 1
#         counts[dna[right]] = counts.get(dna[right]) - 1
#
#         left += 1
#         right += 1
#         while right <= dna_length - 1:
#             counts[dna[left]] = counts.get(dna[left]) + 1
#             counts[dna[right]] = counts.get(dna[right]) + 1
#
#             if is_valid_password():
#                 answer += 1
#
#             counts[dna[left]] = counts.get(dna[left]) - 1
#             counts[dna[right]] = counts.get(dna[right]) - 1
#
#             left += 1
#             right += 1
#
#         print(answer)
#
# ===============================================================

# 다시 체크
check_list = [0] * 4  # 비밀번호 체크 리스트
my_list = [0] * 4  # 현재 상태 리스트
check_secret = 0


def my_add(character: str):
    global check_list, my_list, check_secret
    if character == 'A':
        my_list[0] += 1
        if my_list[0] == check_list[0]:
            check_secret += 1
    elif character == 'C':
        my_list[1] += 1
        if my_list[1] == check_list[1]:
            check_secret += 1
    elif character == 'G':
        my_list[2] += 1
        if my_list[2] == check_list[2]:
            check_secret += 1
    elif character == 'T':
        my_list[3] += 1
        if my_list[3] == check_list[3]:
            check_secret += 1


def my_remove(character: str):
    global check_list, my_list, check_secret
    if character == 'A':
        if my_list[0] == check_list[0]:
            check_secret -= 1
        my_list[0] -= 1
    elif character == 'C':
        if my_list[1] == check_list[1]:
            check_secret -= 1
        my_list[1] -= 1
    elif character == 'G':
        if my_list[2] == check_list[2]:
            check_secret -= 1
        my_list[2] -= 1
    elif character == 'T':
        if my_list[3] == check_list[3]:
            check_secret -= 1
        my_list[3] -= 1


dna_length, secret_length = map(int, input().split())
result = 0
dna = list(input())

check_list = list(map(int, input().split()))

for i in range(4):
    if check_list[i] == 0:
        check_secret += 1

for i in range(dna_length):
    my_add(dna[i])

    if check_secret == 4:
        result += 1

for i in range(dna_length, secret_length):
    j = i - dna_length
    my_add(dna[i])
    my_remove(dna[j])
    if check_secret == 4:
        result += 1

print(result)
