__author__ = 'Martin'

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        sells = [0 for i in range(len(prices))]
        buys = [0 for i in range(len(prices))]
        buys[0] = -prices[0]

        for i in range(1, len(prices)):
            delta = prices[i] - prices[i-1]
            sells[i] = max(buys[i-1]+prices[i], sells[i-1]+delta)
            buys[i] = max(sells[i-2]-prices[i], buys[i-1]-delta)
        return max(sells)

    def maxProfit1(self, prices):
        if len(prices) == 0 or len(prices) == 1:
            return 0
        sells = [0 for i in range(len(prices))]
        buys = [0 for i in range(len(prices))]
        sells[1] = max(0, prices[1] - prices[0])
        buys[1] = max(-prices[0], -prices[1])
        for i in range(2, len(prices)):
            sells[i] = max(sells[i-1], buys[i-1]+prices[i])
            buys[i] = max(buys[i-1], sells[i-2]-prices[i])
        return sells[-1]

s = Solution()
a = [1, 2, 3, 0, 2]
print(s.maxProfit(a))
print(s.maxProfit1(a))