__author__ = 'Martin'

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        m = [None] * size
        l = 1
        m[0] = 0

        for i in range(size):
            low = 0
            high = l

            if nums[m[high-1]] < nums[i]:
                j = high
            else:
                while high - low > 1:
                    mid = (high+low)//2
                    if nums[m[mid-1]] < nums[i]:
                        low = mid
                    else:
                        high = mid
                j = low
            if j == l or nums[i] < nums[m[j]]:
                m[j] = i
                l = max(l, j+1)
        return l


s = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(s.lengthOfLIS(nums))
