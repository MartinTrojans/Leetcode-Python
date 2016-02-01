__author__ = 'Martin'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return
        return self.dp(nums, 0, len(nums)-1)


    def dp(self, nums, low, high):
        mid = (low + high) // 2
        p = TreeNode(nums[mid])
        if mid > low:
            p.left = self.dp(nums, low, mid-1)
        if high > mid:
            p.right = self.dp(nums, mid+1, high)
        return p


s = Solution()
root = s.sortedArrayToBST([1,2,3,4])
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left)
print(root.right.left)