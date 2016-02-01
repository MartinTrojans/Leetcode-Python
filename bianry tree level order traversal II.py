__author__ = 'Martin'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []

        self.bfs(0, root)
        self.res.reverse()

        return self.res

    def bfs(self, level, root):
        if root is not None:
            if len(self.res) < level + 1:
                self.res.append([])
            self.res[level].append(root.val)
            self.bfs(level+1, root.left)
            self.bfs(level+1, root.right)

'''
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1:
                res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)

    def levelOrderBottom(self, root):
        res=[]
        self.preorder(root, 0, res)
        res.reverse()
        return res
'''
s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
res = s.levelOrderBottom(root)
print(res)