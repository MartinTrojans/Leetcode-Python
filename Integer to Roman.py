__author__ = 'Martin'

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        n = [1, 5, 10, 50, 100, 500 ,1000]
        c = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

        for i in range(6, -1, -1):
            temp = num // n[i]
            while temp != 0:
                res += c[i]
                temp -= 1
            num = num % n[i]
            if i == 0:
                break
            if (num + n[(i-1)//2*2]) // n[i] != 0:
                res += c[(i-1)//2*2]
                res += c[i]
                num = (num + n[(i-1)//2*2]) % n[i]
        return res

s = Solution()
print(s.intToRoman(4))