__author__ = 'Martin'

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        sum = l * (l+1) // 2
        x = 0
        for i in nums:
            x += i
        return sum - x

s = Solution()
print(s.missingNumber([1,2,3]))