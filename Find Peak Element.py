__author__ = 'Martin'

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        if low == high:
            return 0
        if high - low == 1:
            if nums[high] > nums[low]:
                return high
            else:
                return low
        return self.bs(nums, low, high)


    def bs(self, nums, low, high):
        mid = low + (high-low) // 2
        if low == 0:
            if nums[1] < nums[0]:
                return 0
        if high == len(nums) - 1:
            if nums[high-1] < nums[high]:
                return high
        if high - low < 2:
            return -1
        if high - low == 2:
            if nums[low] < nums[mid] and nums[high] < nums[mid]:
                return mid
            else:
                return -1
        else:
            b1 = self.bs(nums, low, mid)
            if b1 != -1:
                return b1
            b2 = self.bs(nums, mid, high)
            if b2 != -1:
                return b2
            b3 = self.bs(nums, mid-1, mid+1)
            if b3 != -1:
                return b3
            return -1


    def findPeakElement1(self, num):
        size = len(num)
        return self.search(num, 0, size - 1)

    def search(self, num, start, end):
        if start == end:
            return start
        if start + 1 == end:
            return [start, end][num[start] < num[end]]
        mid = (start + end) / 2
        if num[mid] < num[mid - 1]:
            return self.search(num, start, mid - 1)
        if num[mid] < num[mid + 1]:
            return self.search(num, mid + 1, end)
        return mid

s = Solution()
print(s.findPeakElement([3, 2, 1]))