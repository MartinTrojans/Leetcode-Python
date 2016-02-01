__author__ = 'Martin'


class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        self.dp(None, root, "left")

    def dp(self, p, c, attr):
        if c == None:
            return
        if p == None:
            c.next = None
            self.dp(c, c.left, "left")
            self.dp(c, c.right, "right")
        elif attr == "left":
            c.next = p.right
            self.dp(c, c.left, "left")
            self.dp(c, c.right, "right")
        elif attr == "right":
            if p.next is None:
                c.next = None
            else:
                c.next = p.next.left
            self.dp(c, c.left, "left")
            self.dp(c, c.right, "right")

s = Solution()
root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(3)
s.connect(root)
print(root.next)
print(root.left.next.val)
print(root.right.next)