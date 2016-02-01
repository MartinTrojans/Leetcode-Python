__author__ = 'Martin'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.dfs(root, 0)

    def dfs(self, node, num):
        num = num * 10
        n1 = 0
        n2 = 0
        if node.left is None and node.right is None:
            return num + node.val
        if node.left is not None:
            n1 = self.dfs(node.left, num+node.val)
        if node.right is not None:
            n2 = self.dfs(node.right, num+node.val)
        return n1 + n2

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(2)
root.left.right = TreeNode(2)
root.right = TreeNode(3)
print(s.sumNumbers(root))