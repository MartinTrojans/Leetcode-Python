__author__ = 'Martin'

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        cur = nums[0]
        dis = 0
        id = 0

        for x in range(n):
            id = (id + k) % n
            nums[id], cur = cur, nums[id]

            dis = (dis + k) % n
            if dis == 0:
                id = (id + 1) % n
                cur = nums[id]