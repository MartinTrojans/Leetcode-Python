__author__ = 'Martin'

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.bt(1, n, k)

    def bt(self, s, n, k):
        if n - s < k-1:
            return []
        if k == 1:
            res = []
            for i in range(s, n+1):
                res.append([i])
            return res
        res = []
        for i in range(s, n+1):
            for j in self.bt(i+1, n, k-1):
                res.append([i] + j)
        return res

s = Solution()
print(s.combine(4, 3))