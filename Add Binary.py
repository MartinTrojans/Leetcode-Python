__author__ = 'Martin'

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        flag = 0
        res = ""
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 and j >= 0:
            temp = int(a[i]) + int(b[j]) + flag
            flag = int(temp / 2)
            temp = temp % 2
            res = str(temp) + res
            i -= 1
            j -= 1
        while i >= 0:
            temp = int(a[i]) + flag
            flag = int(temp / 2)
            temp = temp % 2
            res = str(temp) + res
            i -= 1
        while j >= 0:
            temp = int(b[j]) + flag
            flag = int(temp / 2)
            temp = temp % 2
            res = str(temp) + res
            j -= 1
        if flag == 1:
            res = "1" + res
        return res


s = Solution()
print(s.addBinary("1111", "1101"))