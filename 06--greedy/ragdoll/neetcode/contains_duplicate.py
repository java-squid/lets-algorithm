from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number_map = {}

        for number in nums:
            if number in number_map:
                return True
            else:
                number_map[number] = 1

        return False
