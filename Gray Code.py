__author__ = 'Martin'

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self.ans = []
        self.dfs(n, 0, True)
        return self.ans

    def dfs(self, n, res, left):
        if n == 0:
            self.ans.append(res)
            return
        else:
            if left is True:
                self.dfs(n-1, res*2, True)
                self.dfs(n-1, res*2+1, False)
            else:
                self.dfs(n-1, res*2+1, True)
                self.dfs(n-1, res*2, False)

    def grayCode1(self, n):
        res=[]
        size=1<<n
        for i in range(size):
            res.append((i>>1)^i)
        return res

    def grayCode2(self, n):
        if n == 1:
            return [0, 1]
        size = 1 << n
        last = self.grayCode2(n-1)
        res = [0 for i in range(size)]
        for i in range(len(last)):
            res[i] = last[i]
            res[size-1-i] = last[i] + (1<<(n-1))
        return res



'''
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        res=[]
        size=1<<n
        for i in range(size):
            res.append((i>>1)^i)
        return res
'''

s = Solution()
print(s.grayCode(3))
print(s.grayCode1(3))
print(s.grayCode2(3))