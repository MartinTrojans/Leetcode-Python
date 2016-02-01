__author__ = 'Martin'

#Find some more effective method
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == "":
            return 0
        sa = s.split(" ")
        i = len(sa) - 1
        while i >= 0:
            if sa[i] == '':
                i -= 1
                continue
            if sa[i][0] >= 'a' and sa[i][0] <= 'z' or sa[i][0] >= 'A' and sa[i][0] <= 'Z':
                break
            else:
                i -= 1
        j = len(sa[i]) - 1
        num = 0
        flag = 0
        while j >= 0:
            if sa[i][j] >= 'a' and sa[i][j] <= 'z' or sa[i][j] >= 'A' and sa[i][j] <= 'Z':
                flag = 1
                num += 1
                j -= 1
            elif flag == 0:
                j -= 1
                continue
            elif flag == 1:
                break
        return num

s = Solution()
print(s.lengthOfLastWord("Hello World   e "))