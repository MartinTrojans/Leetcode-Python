__author__ = 'Martin'

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        res = [[1]]
        for i in range(1, rowIndex+1):
            row = [1]
            for j in range(1, i):
                row.append(res[i-1][j] + res[i-1][j-1])
            row.append(1)
            res.append(row)
        return res[len(res)-1]