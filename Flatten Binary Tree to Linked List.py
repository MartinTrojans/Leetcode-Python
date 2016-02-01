__author__ = 'Martin'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten1(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.df(root)

    def df(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return root
        if root.left is not None:
            left = self.df(root.left)
        else:
            return self.df(root.right)
        if root.right is not None:
            right = self.df(root.right)
        else:
            right = None
        tmpl = root.left
        tmpr = root.right
        root.right = tmpl
        root.left = None
        left.right = tmpr
        left.left = None
        if right is None:
            return left
        else:
            return right

    def flatten(self, root):
        if root == None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        p = root
        if p.left == None:
            return
        p = p.left
        while p.right:
            p = p.right
        p.right = root.right

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
s.flatten(root)
print(root.right.right.val)