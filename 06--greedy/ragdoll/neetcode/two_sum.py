from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = sorted(nums)
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                if numbers[left] == numbers[right]:
                    left_index = nums.index(numbers[left])
                    right_index = nums.index(numbers[right], left_index + 1)
                    return [left_index, right_index]
                else:
                    return [nums.index(numbers[left]), nums.index(numbers[right])]

            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
