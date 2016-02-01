__author__ = 'Martin'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        cur = root
        pre = None
        while cur is not None:
            if cur.left is None:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right is not None and pre.right != cur:
                    pre = pre.right
                if pre.right is None:
                    res.append(cur.val)
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    cur = cur.right

        return res

s = Solution()
root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(5)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(s.preorderTraversal(root))