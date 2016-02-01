__author__ = 'Martin'

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0

        while j < n:
            if i >= m:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
                i += 1
            else:
                if nums1[i] > nums2[j]:
                    nums1.insert(i, nums2[j])
                    nums1.pop()
                    j += 1
                    m += 1
                else:
                    i += 1

nums1 = [-1,0,0,3,3,0,0,0]
nums2 = [1,2,2]
s = Solution()
s.merge(nums1, 6, nums2, 3)
print(nums1)