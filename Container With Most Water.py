__author__ = 'Martin'

class Solution(object):
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0
        for i in range(len(height)):
            for j in range(j, len(height)):
                temp = (j - i) * min(height[i], height[j])
                if temp > max:
                    max = temp
        return max

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0
        left = 0
        right = len(height) - 1
        while right > left:
            temp = min(height[left], height[right]) * (right - left)
            if temp > max:
                max = temp
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max