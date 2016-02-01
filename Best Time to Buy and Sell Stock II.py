__author__ = 'Martin'

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pro = 0
        i = 0
        lastb = -1
        while i+1 < len(prices):
            if prices[i+1] >= prices[i]:
                pro += prices[i+1] - prices[i]
            i += 1

        return pro

s = Solution()
print(s.maxProfit([1,2,3,4,5,2,3,1]))