from functools import reduce

__author__ = 'Martin'

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(lambda x, y: x ^ y, nums)
        lowbit = xor & (-xor)
        a = b = 0
        for num in nums:
            if lowbit & num:
                a ^= num
            else:
                b ^= num
        return [a, b]

s = Solution()
print(s.singleNumber([2,1,2,1,3,4]))