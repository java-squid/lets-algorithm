class Solution(object):
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for s in str:
            res += str(len(s)) + "#" + s
        return s


    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j]) # # 이후 단어의 길이
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

# 참고
# serializable, deserializable 에 대한 문제인듯.
# str을 encode 하여 보냈을 경우, 받는 쪽에서 어떻게 디코드할것인가.
# 인코드 되어서 오는 str을 어떻게 나눠야하나에 대한 문제

