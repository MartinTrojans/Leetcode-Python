__author__ = 'Martin'

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10 and x >= 0:
            return True
        div = 1
        while x / div >= 10:
            div *= 10

        left = 0
        right = 0
        while x:
            left = x / div
            right = x % 10

            if left != right:
                return False

            x = (x % div) / 10
            div /= 100

        return True