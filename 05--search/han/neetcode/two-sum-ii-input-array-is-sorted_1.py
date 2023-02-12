class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start_pointer = 0
        end_pointer = len(numbers) - 1

        while start_pointer < end_pointer:
            if numbers[start_pointer] + numbers[end_pointer] > target:
                end_pointer -= 1
            elif numbers[start_pointer] + numbers[end_pointer] < target:
                start_pointer += 1
            else:
                return [start_pointer + 1, end_pointer + 1]

        return []


# 문제 해석
# 이미 정렬되어있음.
# 그러면 타겟 이상이면 그 오른쪽 엘리먼트를 체크할 필요가 없어진다.

# sudo code
# two pointer...
# 시간복잡도 O(N)

# 참고
# numbers.length >= 2 -> base case는 필요없지 않을까

