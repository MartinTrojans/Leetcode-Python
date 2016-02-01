import math

__author__ = 'Martin'

class Solution(object):
    def numSquares1(self, n):
        dp = [0]
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]

    def numSquares(self, n):
        while n % 4 == 0:
            n = n //4
        if n % 8 == 7:
            return 4
        i = 0
        while i**2 < n:
            tmp = (int)(math.sqrt(n - i**2))
            if tmp**2 + i**2 == n:
                if tmp != 0 and i!= 0:
                    return 2
                else:
                    return 1
            i += 1
        return 3


s = Solution()
print(s.numSquares(6))