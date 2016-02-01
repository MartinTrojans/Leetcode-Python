__author__ = 'Martin'

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.bt(1, k, n)

    def bt(self, s, k, n):
        if k == 1:
            if n > s-1 and n < 10:
                return [[n]]
            else:
                return []
        res = []
        for i in range(s, 10):
            for j in self.bt(i+1, k-1, n-i):
                res.append([i] + j)
        return res

s = Solution()
print(s.combinationSum3(3, 9))