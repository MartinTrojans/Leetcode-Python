__author__ = 'Martin'

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if len(self.minstack) == 0 or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        x = self.stack.pop()
        if x == self.minstack[-1]:
            self.minstack.pop()
        return x

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]

ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-1)
print(ms.getMin())
print(ms.top())
ms.pop()
print(ms.getMin())