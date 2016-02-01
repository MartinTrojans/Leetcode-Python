__author__ = 'Martin'

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        num = 0
        p = head
        flag = head
        f = 0
        while p is not None:
            p = p.next
            if num == n:
                f = 1
            if num > n:
                flag = flag.next
            else:
                num += 1
        if f == 1:
            flag.next = flag.next.next
        else:
            if head.next is not None:
                head = head.next
            else:
                head = None

        return head

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
s.removeNthFromEnd(head, 1)