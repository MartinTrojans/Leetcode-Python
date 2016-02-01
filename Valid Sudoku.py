__author__ = 'Martin'

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif self.isValidCell(i, j, board) is False:
                    return False

        return True


    def isValidCell(self, x, y, board):
        for i in range(9):
            if y == i:
                continue
            else:
                if board[x][y] == board[x][i]:
                    return False
        for i in range(9):
            if x == i:
                continue
            else:
                if board[x][y] == board[i][y]:
                    return False
        m = int(x / 3) * 3
        n = int(y / 3) * 3
        for i in range(3):
            for j in range(3):
                if x == m+i and y == n+j:
                    continue
                elif board[x][y] == board[m+i][n+j]:
                    return False
        return True




s = Solution()
a = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
print(s.isValidSudoku(a))