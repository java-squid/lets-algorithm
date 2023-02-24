class Solution1:
    def trap(self, height: List[int]) -> int:
        # O(N)
        if len(height) == 1:
            return 0

        max_left = [0] * len(height)
        max_right = [0] * len(height)

        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])

        res = 0

        for i in range(len(height)):
            temp = min(max_left[i], max_right[i]) - height[i]
            if temp < 0:
                continue
            res += temp

        return res


class Solution2:
    def trap(self, height: List[int]) -> int:
        # O(1)
        if len(height) == 1:
            return 0

        l, r = 0, len(height) - 1

        res = 0
        max_l = height[l]
        max_r = height[r]

        while l < r:

            if height[l] < height[r]:
                l += 1
                temp = max_l - height[l]
                if temp > 0:
                    res += temp
                max_l = max(max_l, height[l])
            else:
                # height[l] > height[r] and height[r] == height[r]
                r -= 1
                temp = max_r - height[r]
                if temp > 0:
                    res += temp
                max_r = max(max_r, height[r])

        return res

# 문제 해석
# 어떤 구조물이 있는데, 그 위에 물이 떨어졌음. 그 너비를 구하는 것.

# sudo code
# two pointer..? 시도 -> 실패, 정답 참고.
# min(l, r) - h[i] -> 이러한 풀이법은 제한 시간 내에 생각해낼 수 있었을까? 없었을듯..


# 제한사항
# height.length = 1 인 경우도 있을듯. -> 베이스 케이스로 커버
# n is non negative value
