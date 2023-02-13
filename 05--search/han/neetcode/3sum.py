class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):  # index and value
            if i > 0 and a == nums[i - 1]:
                # 이전 진행했던 것과 같은 값이라면, 중복 때문에 굳이 진행할 필요 없음
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result


# 문제 해석
# 세 수를 더해서 0이 되는 경우를 찾으면 됨.
# 세 수를 더했는데 0이 되는 경우가 없으면 빈 리스트 리턴

# sudo code
# three pointer? -> 못풀었음 답 확인 https://leetcode.com/problems/3sum/submissions/897187151/


# 제한사항
# nums.length >= 3, 무조건 3개 이상 변수 있음.


