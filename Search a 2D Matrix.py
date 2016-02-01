__author__ = 'Martin'

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            if target < matrix[i][-1]:
                for j in range(len(matrix[i])):
                    if matrix[i][j] > target:
                        return False
                    elif matrix[i][j] == target:
                        return True
            elif target == matrix[i][-1]:
                return True
        return False

s = Solution()
print(s.searchMatrix([[1]], 2))