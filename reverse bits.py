__author__ = 'Martin'

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        tmp = 0
        for i in range(32):
            tmp = n & 1
            res <<= 1
            res |= tmp
            n >>= 1
        return res
#can prestore a array of 0x0 - 0xF

s = Solution()
print(s.reverseBits(43261596))