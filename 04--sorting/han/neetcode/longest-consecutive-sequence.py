class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # base case
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        num_set = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in num_set:
                length = 0
                while num + length in num_set:
                    length += 1
                res = max(res, length)
        return res

# nums 내부에 동일한 값이 나올 수도 있는듯.
# O(N) time, space complexity