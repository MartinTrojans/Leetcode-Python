__author__ = 'Martin'


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.instack = []
        self.outstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.instack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.outstack) == 0:
            while len(self.instack) != 0:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.outstack) == 0:
            while len(self.instack) != 0:
                self.outstack.append(self.instack.pop())
        return self.outstack[self.outstack.__len__() - 1]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.outstack) + len(self.instack) == 0:
            return True
        else:
            return False