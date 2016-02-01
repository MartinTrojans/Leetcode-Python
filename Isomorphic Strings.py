__author__ = 'Martin'

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic = dict()
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            else:
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]] = t[i]
        return True
