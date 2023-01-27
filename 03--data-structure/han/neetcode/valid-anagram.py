from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)

        if len(a) != len(b):
            return False

        a_counter = Counter(a)
        b_counter = Counter(b)

        a_counter.subtract(b_counter)

        for k in a_counter:
            if a_counter[k] != 0:
                return False
        return True




# sudo code
# anagram, t 오는 알파벳을 기반으로 s를 다시 만들 수 있는가.


# 제한사항
# 입력값은 모두 lowercase English letters (upper case 신경쓸 필요 없음)
# 1 <= s.length, t.length <= 5 * 10^4 (최대값이 상당히 크다. 타임 리미트..걸릴 수 있을듯)