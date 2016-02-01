__author__ = 'Martin'

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if len(stack) != 0:
                if i == ')' and stack[len(stack)-1] == '(':
                    stack.pop()
                    continue
                elif i == ']' and stack[len(stack)-1] == '[':
                    stack.pop()
                    continue
                elif i == '}' and stack[len(stack)-1] == '{':
                    stack.pop()
                    continue
                else:
                    stack.append(i)
            else:
                stack.append(i)

        if len(stack) != 0:
            return False
        else:
            return True

s = Solution()
print(s.isValid("{[()]}"))