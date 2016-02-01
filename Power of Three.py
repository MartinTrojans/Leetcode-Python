import math

__author__ = 'Martin'

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 1:
            if n % 3 != 0:
                return False
            else:
                n = n / 3
        return True

s = Solution()
print(s.isPowerOfThree(1))