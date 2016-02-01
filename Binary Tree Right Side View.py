from collections import deque

__author__ = 'Martin'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        line1 = deque([])
        line2 = deque([])
        res = []
        line1.append(root)
        while len(line1) > 0 or len(line2) > 0:
            while len(line1) > 0:
                ele = line1.popleft()
                if ele.left is not None:
                    line2.append(ele.left)
                if ele.right is not None:
                    line2.append((ele.right))
            while len(line2) > 0:
                line1.append(line2.popleft())
            res.append(ele.val)
        return res

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
print(s.rightSideView(root))