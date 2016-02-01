__author__ = 'Martin'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        if root is None:
            return
        p = root
        self.stack.append(p)
        while p.left:
            p = p.left
            self.stack.append(p)

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) != 0:
            return True
        else:
            return False


    def next(self):
        """
        :rtype: int
        """
        s = self.stack.pop()
        val = s.val
        if len(self.stack) != 0:
            p = self.stack[-1]
            if s.right is not None:
                p.left = s.right
                while p.left:
                    p = p.left
                    self.stack.append(p)
        else:
            if s.right is not None:
                p = s.right
                self.stack.append(p)
                while p.left:
                    p = p.left
                    self.stack.append(p)
        return val

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(2)
root.left.left.right = TreeNode(3)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(25)
i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())
print(v)