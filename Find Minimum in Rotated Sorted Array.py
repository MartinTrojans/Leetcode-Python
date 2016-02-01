__author__ = 'Martin'

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = nums[0]

        for i in nums[1:]:
            if i < pre:
                return i
        return pre