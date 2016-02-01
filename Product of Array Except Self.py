__author__ = 'Martin'

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0 for i in nums]
        i = 0
        pro = 1
        while i < len(nums):
            res[i] = pro
            pro *= nums[i]
            i += 1
        pro = 1
        i = len(nums) - 1
        while i > -1:
            res[i] *= pro
            pro *= nums[i]
            i -= 1
        return res

s = Solution()
print(s.productExceptSelf([1,2,3,4]))