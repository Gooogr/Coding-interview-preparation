# https://leetcode.com/problems/container-with-most-water/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            # Water amount - area between two bins. 
            # And height if this area is limited by smaller bin
            current_area = (r -l) * min(height[l], height[r])
            max_area = max(max_area, current_area)
            # Try to find bigger bin for the samller one in pair.
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
