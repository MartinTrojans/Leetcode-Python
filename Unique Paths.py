__author__ = 'Martin'

'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.res = 0
        self.dfs(m, n)
        return self.res

    def dfs(self, m, n):
        if m == 1 and n == 1:
            self.res += 1
        if m > 1:
            self.dfs(m-1, n)
        if n > 1:
            self.dfs(m, n-1)
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1:
            return 1
        if n == 1:
            return 1
        dp = [[0 for i in range(n)] for i in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

s = Solution()
print(s.uniquePaths(3, 7))