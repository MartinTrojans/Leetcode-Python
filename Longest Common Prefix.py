__author__ = 'Martin'

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        temp = ""
        lmin = 100000
        flag = 1
        if len(strs) == 0:
            return ""
        for i in strs:
            if len(i) < lmin:
                lmin = len(i)
        for i in range(lmin):
            if len(strs[0]) > i:
                temp = strs[0][i]
            else:
                return res
            for str in strs:
                if str[i] != temp:
                    flag = 0
                    break
            if flag != 0:
                res += temp
            else:
                break
        return res

s = Solution()
strs = ["hahaha", "haha", "ha"]
print(s.longestCommonPrefix(strs))