class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        empty_index = 0

        for str in strs:
            if not str:
                # if str[i].length = 0
                anagrams[empty_index].append("")
            else:
                anagrams[''.join(sorted(str))].append(str)
        return list(anagrams.values())

# 문제 이해

# 수도 코드

# 제한 사항
# strs.length >= 1, 0으로 들어오는 케이스 없음.
# 다만 strs[i] => 0 0으로 들어오는 케이스 있음. 즉 [""] 케이스