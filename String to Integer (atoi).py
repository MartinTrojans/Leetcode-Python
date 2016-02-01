__author__ = 'Martin'

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str is None:
            return 0
        if str == "":
            return 0
        i = 0
        num = ""
        while i < len(str):
            if str[i] == "+" and i+1 < len(str):
                if ord(str[i+1]) >= ord("0") and ord(str[i+1]) <= ord("9"):
                    i += 1
                    while i < len(str) and ord(str[i]) >= ord("0") and ord(str[i]) <= ord("9"):
                        num += str[i]
                        i += 1
                    if int(num) > 2147483647:
                        return 2147483647
                    else:
                        return int(num)
                else:
                    return 0
            if str[i] == "-" and i+1 < len(str):
                if ord(str[i+1]) >= ord("0") and ord(str[i+1]) <= ord("9"):
                    i += 1
                    while i < len(str) and ord(str[i]) >= ord("0") and ord(str[i]) <= ord("9"):
                        num += str[i]
                        i += 1
                    if int(num) > 2147483648:
                        return -2147483648
                    else:
                        return -int(num)
                else:
                    return 0
            if ord(str[i]) >= ord("0") and ord(str[i]) <= ord("9"):
                while i < len(str) and ord(str[i]) >= ord("0") and ord(str[i]) <= ord("9"):
                    num += str[i]
                    i += 1
                if int(num) > 2147483647:
                    return 2147483647
                else:
                    return int(num)
            if str[i].isalpha():
                return 0
            i += 1
        return 0

s = Solution()
print(s.myAtoi("        010"))