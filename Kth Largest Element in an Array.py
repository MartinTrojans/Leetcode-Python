import heapq

__author__ = 'Martin'

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums1 = []
        nums2 = []
        pivot = nums[0]
        for i in nums[1:]:
            if i < pivot:
                nums1.append(i)
            else:
                nums2.append(i)
        l1 = len(nums1)
        l2 = len(nums2)
        if k > l2+1:
            return self.findKthLargest(nums1, k-l2-1)
        elif k < l2+1:
            return self.findKthLargest(nums2, k)
        else:
            return pivot

    def findKthLargest1(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]

    def findKthLargest2(self, nums, k):
        heap = []
        for i in nums:
            heap.append(-i)
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return -heap[0]

s = Solution()
nums = [1,2,3,4,5,2,3,4,1,6]
print(s.findKthLargest2(nums, 3))