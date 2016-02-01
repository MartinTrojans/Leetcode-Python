__author__ = 'Martin'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    nodelist = []
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        strs = []
        self.dfs(root, [])
        for list in self.nodelist:
            string = ""
            for i in range(len(list)):
                if i == 0:
                    string += str(list[i])
                else:
                    string += "->" + str(list[i])
            strs.append(string)
        return strs


    def dfs(self, root, path):
        if root is None:
            return
        path.append(root.val)
        rightpath = list(path)
        if root.left is None and root.right is None:
            self.nodelist.append(path)
        self.dfs(root.left, path)
        self.dfs(root.right, rightpath)

    def binaryTreePaths1(self, root):
        self.ans = []
        if root is None:
            return self.ans
        def dfs(root, path):
            if root.left is None and root.right is None:
                self.ans += path,
            if root.left:
                dfs(root.left, path + "->" + str(root.left.val))
            if root.right:
                dfs(root.right, path + "->" + str(root.right.val))
        dfs(root, str(root.val))
        return self.ans

s = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t5 = TreeNode(5)
t1.left = t2
#t1.right = t3
#t2.right = t5
print(s.binaryTreePaths(t1))