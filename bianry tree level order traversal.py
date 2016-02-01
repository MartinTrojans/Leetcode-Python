__author__ = 'Martin'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        self.bfs(0, root)
        return self.res

    def bfs(self, level, root):
        if root is None:
            return
        if len(self.res) <= level:
            self.res.append([])
        self.res[level].append(root.val)
        self.bfs(level+1, root.left)
        self.bfs(level+1, root.right)


s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
res = s.levelOrder(root)
print(res)