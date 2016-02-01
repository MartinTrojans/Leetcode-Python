__author__ = 'Martin'

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size <= 2:
            return size
        flag = False
        pre = nums[0]
        i = 1
        while i < len(nums):
            if flag:
                if nums[i] != pre:
                    flag = False
                else:
                    size -= 1
                    del nums[i]
                    i -= 1
            else:
                if nums[i] == pre:
                    flag = True
            pre = nums[i]
            i += 1
        return size

    def removeDuplicates1(self, A):
        if len(A) <= 2: return len(A)
        prev = 1; curr = 2
        while curr < len(A):
            if A[curr] == A[prev] and  A[curr] == A[prev - 1]:
                curr += 1
            else:
                prev += 1
                A[prev] = A[curr]
                curr += 1
        return prev + 1

s = Solution()
nums = [1,1,1,1,2,2,2,2,3]
print(s.removeDuplicates(nums))
print(nums)