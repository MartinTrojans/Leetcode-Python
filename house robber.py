__author__ = 'Martin'


class Solution(object):
    '''
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.max(len(nums)-1, nums)


    def max(self, i, nums):
        if i < 0:
            return 0
        if i == 0:
            return nums[0]
        m1 = self.max(i-1, nums)
        m2 = self.max(i-2, nums) + nums[i]
        if m1 > m2:
            return m1
        else:
            return m2
    '''
    '''
    def rob(self, nums):
        l = len(nums)
        dp = [0] * (l+1)
        if l:
            dp[1] = nums[0]
        for i in range(2, l+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        return dp[l]
        '''
    def rob(self, nums):
        l = len(nums)
        odd, even = 0, 0
        for i in range(l):
            if i % 2:
                odd = max(even, odd + nums[i])
            else:
                even = max(odd, even + nums[i])
        return max(odd, even)

s = Solution()
nums = [2,1]
print(s.rob(nums))
