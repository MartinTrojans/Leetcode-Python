__author__ = 'Martin'

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numsDict = dict()
        for i in range(len(nums)):
            ib = numsDict.get(nums[i])
            if ib is not None:
                if i - ib <= k:
                    return True
            numsDict[nums[i]] = i
        return False

s = Solution()
a = [1,0,1,1]
k = 1
print(s.containsNearbyDuplicate(a, k))