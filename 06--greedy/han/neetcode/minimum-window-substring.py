class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # count_t 는 char이 얼마나 들어있는지 count하는 맵
        # window 는 현재 window에서 char이 얼마나 들어있는지 count하는 맵
        count_t, window = {}, {}

        # count_t initialize
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        # have, 현재 윈도우에서 t에 속하는 char 갯수를 얼마나 갖고 있는가 (숫자)
        # need = 필요한 char의 숫자
        # 매번 map을 모두 iterate 하는 것은 비율적.
        # 현재 window가 가지고 있는 타겟 갯수와, 필요한 캐릭터 갯수를 비교함으로써 linear time 으로 알고리즘을 해결할 수 있을듯
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("infinity")

        # left pointer
        l = 0

        # r right pointer
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # char이 카운트를 해야하는 대상이고, 그 갯수도 일치한다면..
            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # pop from left of window
                # decrease count
                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if res_len != float("infinity") else ""

# 문제해석
# 어렵다.
# t로 들어오는 문자열 중에 , s가 포함되는 window case의 char을 리턴하는 문제인듯.
# 그런데, example 3 와 같은 경우는 empty string을 리턴해야하고. (잘 이해안됨)

# sudo code
# keyword -> hashmap, two pointer

# 제한
# t.length >= 1... empty일 경우를 체크할 필요는 없을듯

# 피드백
# 해석을 봐도 어렵다. 풀이하는 방법을 코드로 잘 풀어나가야하는데 이게 좀 아직은 힘든듯
