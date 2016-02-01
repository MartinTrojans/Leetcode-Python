__author__ = 'Martin'


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        low = 0
        high = n
        while high - low > 1:
            mid = low + (high-low)//2
            if mid * mid <= n:
                low = mid
            else:
                high = mid
        return low

s = Solution()