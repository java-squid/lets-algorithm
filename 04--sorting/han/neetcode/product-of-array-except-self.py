class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        left = [0] * length
        right = [0] * length
        res = [0] * length

        left[0] = 1
        right[length - 1] = 1

        # left [1, 1, 2, 6]
        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]

        # right [24 ,12, 4, 1]
        for j in range(length - 2, -1, -1):
            right[j] = right[j + 1] * nums[j + 1]

        for i in range(length):
            res[i] = left[i] * right[i]

        return res


# 제한사항
# 시간복잡도 O(N), 공간복잡도 O(N)..
# 공간복잡도를 O(1) 으로 줄일 수 있을까?