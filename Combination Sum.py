__author__ = 'Martin'

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.bt(candidates, target)

    def bt(self, candidates, target):
        res = []
        for i in range(len(candidates)):
            if candidates[i] == target:
                res.append([candidates[i]])
            elif candidates[i] > target:
                break
            else:
                for j in self.bt(candidates[i:], target-candidates[i]):
                    res.append([candidates[i]]+j)
        return res

s = Solution()
print(s.combinationSum([8,7,4,3], 11))