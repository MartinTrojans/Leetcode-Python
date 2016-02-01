import math

__author__ = 'Martin'
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str = ""
        for c in s:
            if c >= 'a' and c <= 'z' or c >= 'A' and c <='Z' or c >= '0' and c <= '9':
                str += c.lower()
        length = len(str)
        for i in range(int(math.floor(length / 2))):
            if str[i] != str[len(str)-1-i]:
                return False
        return True
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        end = len(s) - 1
        start = 0
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
