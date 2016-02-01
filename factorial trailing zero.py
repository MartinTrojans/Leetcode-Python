__author__ = 'Martin'


#De Polignac's formula
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        num = 0
        temp = 5
        while temp <= n:
            num += n / temp
            i += 1
            temp = pow(5, i)
        return  num