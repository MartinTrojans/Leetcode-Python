__author__ = 'Martin'

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        j = 0
        flag = i
        if needle == "":
            return 0
        if haystack is "":
            return -1

        while i < len(haystack):
            if haystack[i] == needle[j]:
                flag = i
                while j < len(needle):

                    if i >= len(haystack):
                        return -1
                    if haystack[i] != needle[j]:
                        j = 0
                        i = flag
                        break
                    i += 1
                    j += 1
                if j == len(needle):
                    return flag
            i += 1
        return -1

s = Solution()
print(s.strStr("a", ""))
