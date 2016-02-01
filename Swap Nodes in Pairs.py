__author__ = 'Martin'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        if head.next is None:
            return head
        else:
            newhead = head.next
        p = head
        while p.next is not None:
            next = p.next.next
            pre = p
            p.next.next = p
            pre.next = next
            pre = p
            p = pre.next
            if p is None:
                break
            if p.next is not None:
                pre.next = p.next

        return newhead

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs1(self, head):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0); dummy.next = head
        p = dummy
        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(s.swapPairs(head))