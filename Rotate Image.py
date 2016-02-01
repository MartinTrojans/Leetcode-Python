import math

__author__ = 'Martin'

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        num = (int)(math.ceil((n+1) / 2))
        for i in range(num):
            for j in range(i, len(matrix)-1-i):
                matrix[j][n-i], matrix[n-i][n-j], matrix[n-j][i], matrix[i][j] = \
                    matrix[i][j], matrix[j][n-i], matrix[n-i][n-j], matrix[n-j][i]

    def rotate1(self, matrix):
        #先转置，后反转
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix

s = Solution()
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
s.rotate(matrix)
print(matrix)