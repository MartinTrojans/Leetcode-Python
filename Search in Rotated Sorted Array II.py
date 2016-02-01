__author__ = 'Martin'

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        index = 0
        if size == 0:
            return False
        for i in range(1, size):
            if nums[i] < nums[i-1]:
                index = i
                break
        nums = nums[index:] + nums[:index]
        low = 0
        high = size-1
        while high >= low:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

    def search1(self, nums, target):
        size = len(nums)
        index = 0
        if size == 0:
            return False
        left = 0
        right = len(nums) - 1
        mid = (left+right) // 2
        while left <= right:
            if nums[mid] == target:
                return True
            if nums[left] < nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
            mid = (left+right) // 2
        return False

s = Solution()
print(s.search1([2,3,4,5,6,0,1,2],1))