__author__ = 'Martin'

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = None
        p = head
        while p is not None:
            if p.val == val:
                if p == head:
                    head = head.next
                    p = head
                else:
                    pre.next = p.next
                    p = pre.next
                continue
            pre = p
            p = p.next

        return head
