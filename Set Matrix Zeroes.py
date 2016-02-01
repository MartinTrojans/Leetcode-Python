__author__ = 'Martin'

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        fr = 0
        fc = 0
        m = len(matrix)
        flag = False
        if m == 0:
            return matrix
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    fr = i
                    fc = j
                    flag = True
                    break
            if matrix[i][j] == 0:
                break
        if flag == False:
            return
        for i in range(fr+1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[fr][j] = 0
                    matrix[i][fc] = 0
        for i in range(fr+1, m):
            if matrix[i][fc] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for i in range(n):
            if matrix[fr][i] == 0:
                for j in range(m):
                    matrix[j][i] = 0
        for i in range(n):
            matrix[fr][i] = 0

s = Solution()
matrix = [
    [1,2,0,3],
    [0,1,3,4],
    [1,2,3,4]
]
matrix1 = [[1]]
s.setZeroes(matrix1)
print(matrix1)