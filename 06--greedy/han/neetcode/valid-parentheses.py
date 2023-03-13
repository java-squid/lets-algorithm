class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        char_type = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c not in char_type:  # (, {, [
                stk.append(c)
            elif not stk:
                return False
            else:
                # c = ), }, ]
                if stk.pop() != char_type[c]:
                    return False

        return len(stk) == 0

# 문제해석
# input값 s는 (, ) {, }, [, ] 만 가지고 있음.
# ( 이면 반드시 )로 닫혀야함 -> stack

# sudo code
# stack 이용
# char_type map 형태로 생성해두기 (이런 형식만 입력되니까, 미리 생성해놓는게 나을듯)

# 기타
# O(N)