__author__ = 'Martin'

class Solution(object):
    def subsets1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        return [[]] + self.bt(nums)

    def bt(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            res.append([nums[i]])
            for j in self.bt(nums[i+1:]):
                res.append([nums[i]] + j)
        return res

    def subsets(self, S):
        def dfs(depth, start, valuelist):
            res.append(valuelist)
            if depth == len(S): return
            for i in range(start, len(S)):
                dfs(depth+1, i+1, valuelist+[S[i]])
        S.sort()
        res = []
        dfs(0, 0, [])
        return res

s = Solution()
print(s.subsets([1,2,3,4]))