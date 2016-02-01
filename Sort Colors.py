__author__ = 'Martin'


class Solution(object):
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums) - j:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                nums[1:] = nums[0:len(nums)-1]
                nums[0] = 0
            elif nums[i] == 2:
                del nums[i]
                nums.append(2)
                j += 1
                i -= 1
            i += 1
    def sortColors(self, nums):
        p0 = 0
        p2 = len(nums)-1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1
            elif nums[i] == 2:
                nums[p2], nums[i] = nums[i], nums[p2]
                p2 -= 1
                i -= 1
            i += 1

s = Solution()
nums = [1,1,0,0,0,0,1,2,0,1,2]
s.sortColors(nums)
print(nums)