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
            return -1
        for i in range(1, size):
            if nums[i] == target:
                return i
            if nums[i] < nums[i-1]:
                index = i
                break
        nums = nums[index:] + nums[:index]
        low = 0
        high = size-1
        while high >= low:
            mid = (low + high) // 2
            if nums[mid] == target:
                return (mid + index) % size
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def search1(self, A, target):
        left = 0; right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if target == A[mid]:
                return mid
            if A[mid] >= A[left]:
                if target < A[mid] and target >= A[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif A[mid] < A[right]:
                if target > A[mid] and target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1



    '''
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return -1
        for i in range(size):
            if nums[i] == target:
                return i
        return -1
    '''
s = Solution()
nums = [4,5,6,7,8,0,1,2,3]
print(s.search(nums, 8))