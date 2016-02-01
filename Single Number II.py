__author__ = 'Martin'

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0
        two = 0
        three = 0
        for i in nums:
            two |= one & i
            one ^= i
            three = ~(one & two)
            one &= three
            two &= three

        return one

s = Solution()
print(s.singleNumber([1,1,1,2,2,2,3]))