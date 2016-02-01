__author__ = 'Martin'

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return self.dp(len(grid)-1, len(grid[0])-1, grid)

    def dp(self, i, j, grid):
        if i == 0 and j == 0:
            return grid[i][j]
        if i == 0:
            return self.dp(i, j-1, grid) + grid[i][j]
        if j == 0:
            return self.dp(i-1, j, grid) + grid[i][j]
        return min(self.dp(i-1, j, grid)+grid[i][j], self.dp(i, j-1, grid) + grid[i][j])

    def minPathSum1(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])
        return dp[-1][-1]

s = Solution()
grid = [
    [1,2,3,4],
    [2,3,4,1],
    [2,3,7,4]
]
print(s.minPathSum1(grid))