__author__ = 'Martin'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.val = -1
        self.dfs(root, k)
        return self.val


    def dfs(self, node, k):
        if node.left is None and node.right is None:
            self.count += 1
            if self.count == k:
                self.val = node.val
            return
        if node.left is not None:
            self.dfs(node.left, k)
        self.count += 1
        if self.count == k:
            self.val = node.val
        if node.right is not None:
            self.dfs(node.right, k)

    def kthSmallest1(self, root, k):
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        x = 1
        while stack and x <= k:
            node = stack.pop()
            x += 1
            right = node.right
            while right:
                stack.append(right)
                right = right.left
        return node.val

    def kthSmallest2(self, root, k):
        '''
        count the left nodes
        '''

s = Solution()
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)
print(s.kthSmallest(root, 3))
print(s.kthSmallest1(root, 3))