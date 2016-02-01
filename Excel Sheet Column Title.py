__author__ = 'Martin'

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        str = ""
        stack = []
        while n // 26 != 0:
            stack.append(n % 26)
            n = n // 26
        stack.append(n % 26)
        i = 0
        while i < len(stack):
            if stack[i] == 0:
                if i+1 < len(stack):
                    stack[i] = 26
                    stack[i+1] -= 1
            i += 1
        if stack[-1] == 0:
            stack.pop()
        while len(stack) != 0:
            x = stack.pop()
            str += chr((x - 1) + ord("A"))
        return str

s = Solution()
print(s.convertToTitle(26))