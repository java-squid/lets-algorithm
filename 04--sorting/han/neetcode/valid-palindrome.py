class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # removing all space
        s = s.replace(" ", "")

        if len(s) == 0:
            return True

        # converting all uppercase letters into lowercase letters
        s = s.lower()

        # removing all non-alphanumeric characters
        s = ''.join(filter(str.isalnum, str(s)))

        return s == s[::-1]
