__author__ = 'Martin'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow = head
        fast = head
        while fast is not None and slow is not None:
            slow = slow.next
            if fast.next is None:
                return False
            fast = fast.next.next
            if slow == fast:
                return True
        return False

s = Solution()
head = ListNode(1)
head.next = head
print(s.hasCycle(head))