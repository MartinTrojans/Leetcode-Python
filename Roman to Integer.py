__author__ = 'Martin'

class Solution(object):
    def romanToInt1(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = [1, 5, 10, 50, 100, 500, 1000]
        r = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        res = 0
        size = len(s)
        for j in range(size):
            if j < size-1:
                if r.index(s[j]) < r.index(s[j+1]):
                    res -= i[r.index(s[j])]
                else:
                    res += i[r.index(s[j])]
            else:
                res += i[r.index(s[j])]
        return res

    def romanToInt(self, s):
        numerals = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        sum=0
        s=s[::-1]
        last=None
        for x in s:
            if last and numerals[x]<last:
                sum-=2*numerals[x]
            sum+=numerals[x]
            last=numerals[x]
        return sum

str = "DCXXI"
s = Solution()
print(s.romanToInt(str))