__author__ = 'Martin'

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic = dict()
        strs = str.split(" ")
        if len(pattern) != len(strs):
            return False
        for i in range(len(strs)):
            if (pattern[i] in dic) is False:
                if strs[i] in dic.values():
                    return False
                dic[pattern[i]] = strs[i]
            elif dic[pattern[i]] != strs[i]:
                return False
        return True

s = Solution()
pattern = 'abba'
str = "dog cat cat dog"
print(s.wordPattern(pattern, str))