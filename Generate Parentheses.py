from collections import Set

__author__ = 'Martin'

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        self.dfs(n, n, "", res)
        return res

    def dfs(self, l, r, str, res):
        if r < l:
            return
        elif r == 0 and l == 0:
            res.append(str)
        if l > 0:
            self.dfs(l-1, r, str+"(", res)
        if r > 0:
            self.dfs(l, r-1, str+")", res)

s = Solution()
print(s.generateParenthesis(3))
