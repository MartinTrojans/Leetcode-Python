__author__ = 'Martin'

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        dir = 0
        l = n * n
        num = n
        cur = 1
        res = [[0 for i in range(n)] for i in range(n)]
        i = 0
        j = 0
        while num > 0:
            count = 0
            if dir == 0:
                while count < num:
                    res[i][j] = cur
                    count += 1
                    cur += 1
                    j += 1
                j -= 1
                i += 1
                num -= 1
            elif dir == 1:
                while count < num:
                    res[i][j] = cur
                    count += 1
                    cur += 1
                    i += 1
                i -= 1
                j -= 1
            elif dir == 2:
                while count < num:
                    res[i][j] = cur
                    count += 1
                    cur += 1
                    j -= 1
                j += 1
                i -= 1
                num -= 1
            elif dir == 3:
                while count < num:
                    res[i][j] = cur
                    count += 1
                    cur += 1
                    i -= 1
                i += 1
                j += 1
            dir = (dir + 1) % 4
        return res


s = Solution()
print(s.generateMatrix(4))