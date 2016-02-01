__author__ = 'Martin'

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tempsum = 0
        maxsum = nums[0]

        for i in nums:
            if tempsum < 0:
                tempsum = 0
            tempsum += i
            maxsum = max(tempsum, maxsum)
        return maxsum