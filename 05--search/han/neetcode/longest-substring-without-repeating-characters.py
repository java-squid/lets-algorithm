class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)

        return res

# 문제 이해
# 반복 되는 문자열 없는 가장 긴 문자열의 길이를 반환
# two pointer
# set의 구조를 이용

# 참고
# len(s) == 0 인 케이스가 있는듯.