__author__ = 'Martin'

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.maxp = 0
        if len(prices) == 0:
            return 0
        min = prices[0]
        max = 0
        sub = 0
        for i in prices[1:]:
            if i < min:
                min = i
            else:
                sub = i - min
            if sub > max:
                max = sub
        return max

s = Solution()
print(s.maxProfit([1,2,3,4,5,2,3,4,5,1,2321,213,4]))