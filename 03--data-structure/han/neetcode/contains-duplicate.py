# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        mset = set(nums)

        if len(nums) != len(mset):
            return True

        return False
