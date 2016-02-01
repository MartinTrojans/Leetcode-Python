__author__ = 'Martin'

from collections import deque

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = deque([])

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        l = len(self.queue)
        for i in range(len(self.queue)):
            top = self.queue.popleft()
            if i == l - 1:
                break
            self.queue.append(top)
        #return top

    def top(self):
        """
        :rtype: int
        """
        top = None
        for i in range(len(self.queue)):
            top = self.queue.popleft()
            self.queue.append(top)
        return top

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.queue) == 0:
            return True
        else:
            return False

s = Stack()
s.push(1)
s.push(2)
s.pop()
print(s.top())