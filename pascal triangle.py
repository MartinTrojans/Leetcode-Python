__author__ = 'Martin'

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(res[i-1][j] + res[i-1][j-1])
            row.append(1)
            res.append(row)
        return res

s = Solution()
print(s.generate(5))