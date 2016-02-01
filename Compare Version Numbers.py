__author__ = 'Martin'

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        str1 = version1.split(".");
        str2 = version2.split(".");
        i = 0
        while i < len(str1) and i < len(str2):
            if int(str1[i]) > int(str2[i]):
                return 1
            elif int(str1[i]) < int(str2[i]):
                return -1
            i += 1
        amount = 0
        if len(str1) > len(str2):
            for i in str1[i:len(str1)]:
                amount += int(i)
            if amount != 0:
                return 1
        elif len(str1) < len(str2):
            for i in str2[i:len(str2)]:
                amount += int(i)
            if amount != 0:
                return -1
        return 0

s = Solution()
print(s.compareVersion("1.0.0.0.1", "1"))