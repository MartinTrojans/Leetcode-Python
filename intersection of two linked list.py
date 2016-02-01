__author__ = 'Martin'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = 0
        l2 = 0
        p1 = headA
        p2 = headB
        while p1 is not None:
            l1 += 1
            p1 = p1.next
        while p2 is not None:
            l2 += 1
            p2 = p2.next
        dif = l1 - l2
        p1 = headA
        p2 = headB
        if dif < 0:
            while dif < 0:
                p2 = p2.next
                dif += 1
        if dif > 0:
            while dif > 0:
                p1 = p1.next
                dif -= 1

        while p1 is not None and p2 is not None:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next

        return None
#http://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/