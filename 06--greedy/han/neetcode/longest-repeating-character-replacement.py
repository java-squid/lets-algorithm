class Solution:
    # O(N)
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        counter = {}
        res = 0
        l = 0
        max_frequency = 0

        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            max_frequency = max(max_frequency, counter[s[r]])

            if (r - l + 1) - max_frequency > k:
                counter[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

# 문제해석
# s는 string, 최대 k번째까지 아무 캐릭터나 골라서 변경할 수 있음.
# str의 캐릭터를 최대 k만큼 변경해서 substring이 가장 긴 경우를 찾아내야함.
# 반례 s = "ABBB", k = 2 일 경우 4가 나오지 않음.. -> 어떻게 개선해야할지 모르겠다.
# 히스토리 https://leetcode.com/problems/longest-repeating-character-replacement/submissions/908330577/

# sudo code
# 실제 character를 바꾸는 것을 의도한 건 아닌듯.

# 제한
# s.length = 1 일수 있음.


class Solution:
    # O(26 * N)
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        counter = {}
        res = 0 # minimize
        l = 0

        for r in range(len(s)):
            c = s[r]
            counter[c] = 1 + counter.get(c, 0)

            while (r - l + 1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
