__author__ = 'Martin'

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        if fast is None:
            return None
        if fast.next is None:
            return None
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                break
        if fast.next == None or fast.next.next == None:
            return None
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow

s = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next
print(s.detectCycle(head))