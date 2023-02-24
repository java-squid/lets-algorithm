# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         # brute force -> time limited exceed
#         res = 0
#
#         for l in range(len(height)):
#             for r in range(l + 1, len(height)):
#                 area = (r - l) * min(height[l], height[r])
#                 res = max(res, area)
#
#         return res

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer
        res = 0

        l = 0
        r = len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] > height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
            else:
                l += 1

        return res



# 문제 해석
# 어떤 area를 만들어서, 가장 큰 너비를 구하는 방법.
# 어떻게 풀어야할까?

# sudo code
# 못풀었음 답
# 1. 모든 경우의 수를 찾는 방법 Brute force -> 시간 초과
# 2. two pointer, 특정 조건을 만족하는 경우 l, r pointer 움직인다.
# 특정 조건, 두 개의 포인터가 가르키고 있는 높이 중, 낮은 걸 옮긴다.
# 옮기면서 너비를 각각 계산하고, 그 중 가장 큰 값을 리턴.
# 너비를 구하는 방법 (width * height)


# 제한사항


