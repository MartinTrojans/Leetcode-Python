__author__ = 'Martin'

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = "1"

        for i in range(n-1):
            res = ""
            pre = ""
            for c in num:
                if pre != c:
                    if pre != "":
                        res += str(count) + pre
                    count = 1
                    pre = c
                else:
                    count += 1
            num = res + str(count) + pre
        return num

s = Solution()
print(s.countAndSay(5))