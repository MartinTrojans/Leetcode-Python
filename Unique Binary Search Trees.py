__author__ = 'Martin'

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = [1 for i in range(n+1)]
        for j in range(2, n+1):
            sum = 0
            for i in range(j):
                sum += c[i] * c[j-1-i]
            c[j] = sum
        return c[n]

s = Solution()
print(s.numTrees(19))