__author__ = 'Martin'

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        return self.dp(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1, target)


    def dp(self, matrix, rowl, rowh, coll, colh, target):
        if rowl > rowh or coll > colh:
            return False
        rmid = (rowl+rowh)//2
        cmid = (coll+colh)//2
        if matrix[rmid][cmid] == target:
            return True
        elif matrix[rmid][cmid] > target:
            return self.dp(matrix, rowl, rmid-1, coll, cmid-1, target) or self.dp(matrix, rmid, rowh, coll, cmid-1, target) \
                   or self.dp(matrix, rowl, rmid-1, cmid, colh, target)
        else:
            return self.dp(matrix, rmid+1, rowh, cmid+1, colh, target) or self.dp(matrix, rmid+1, rowh, coll, cmid, target) \
                   or self.dp(matrix, rowl, rmid, cmid+1, colh, target)

s = Solution()
matrix = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
print(s.searchMatrix(matrix, 20))