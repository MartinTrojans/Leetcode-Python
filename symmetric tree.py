__author__ = 'Martin'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.Symmetric(root.left, root.right)

    def Symmetric(self, root1, root2):
        if root1 == root2 and root1 is None:
            return True
        if root1.left == root2.right and root1.right == root2.left:
            return self.Symmetric(root1.left, root2.right) and self.Symmetric(root1.right, root2.left)
        else:
            return False