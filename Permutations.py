from copy import deepcopy

__author__ = 'Martin'

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            for j in self.permute(nums[:i]+nums[i+1:]):
                res.append([nums[i]] + j)

        return res


s = Solution()
print(s.permute([1,2,3]))