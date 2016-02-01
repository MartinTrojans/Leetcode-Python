__author__ = 'Martin'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.bfs(root, 0)

    def bfs(self, root, level):
        if root is None:
            return level
        if root.left is None and root.right is None:
            return  level + 1
        elif root.left is None or root.right is None:
            return max(self.bfs(root.left, level+1), self.bfs(root.right, level+1))
        else:
            return min(self.bfs(root.left, level+1), self.bfs(root.right, level+1))
    '''
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right != None:
            return self.minDepth( root.right ) + 1
        if root.left != None and root.right == None:
            return self.minDepth( root.left ) + 1
        return min( self.minDepth( root.left ), self.minDepth( root.right ) ) + 1
    '''

t = TreeNode(1)
t.left = TreeNode(2)
s = Solution()
print(s.minDepth(t))