__author__ = 'Martin'

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        num = 0
        if x < 0:
            x = -x
            flag = -1
        while x > 0:
            num  = num * 10 + x % 10
            x = int(x / 10)
        return flag * num

s = Solution()
print(s.reverse(-123))