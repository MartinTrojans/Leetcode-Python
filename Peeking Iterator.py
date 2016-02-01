__author__ = 'Martin'

class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.peeked = False
        self.peekele = -1
        self.it = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peeked is False:
            self.peeked = True
            self.peekele = self.it.next()
        return self.peekele


    def next(self):
        """
        :rtype: int
        """
        if self.peeked is True:
            self.peeked = False
            return self.peekele
        else:
            return self.it.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peeked or self.it.hasNext()

nums = [1,2,3,4]
iter = PeekingIterator(Iterator(nums))
while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    iter.next()         # Should return the same value as [val].