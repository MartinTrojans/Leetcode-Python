__author__ = 'Martin'

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        lists = ["" for i in range(numRows)]
        row = 0
        i = 0
        while i < len(s):
            while row < numRows:
                if i < len(s):
                    lists[row] += s[i]
                    row += 1
                    i += 1
                else:
                    break
            row = numRows - 2
            while row >= 0:
                if i < len(s):
                    lists[row] += s[i]
                    row -= 1
                    i += 1
                else:
                    break
            row = 1
        res = ""
        for i in range(numRows):
                res += lists[i]
        return res

s = Solution()
print(s.convert("ab", 1))