__author__ = 'Martin'

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        strs = []
        temp = []
        last = nums[0]
        temp.append(last)
        for n in nums[1:len(nums)]:
            if n == last + 1:
                temp.append(n)
                last = n
            else:
                if len(temp) == 1:
                    strs.append(str(temp[0]))
                else:
                    strs.append(str(temp[0]) + "->" + str(temp[len(temp)-1]))
                temp = []
                temp.append(n)
                last = n
        if len(temp) == 1:
            strs.append(str(temp[0]))
        else:
            strs.append(str(temp[0]) + "->" + str(temp[len(temp)-1]))
        return strs

s = Solution()
nums = [1,2,4,5,7]
print(s.summaryRanges(nums))