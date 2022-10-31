# https://leetcode.com/problems/trapping-rain-water/

# Computation O(n), memory O(1)
# Idea: water_level[i] = min(max_left, max_right) - h[i]
# With two pointers we track minimum height of walls. Since water will leak only in one direction (or  # just leak out completely from the flat surface), we are interested only in the current maximum for 
# every step.
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) -1
        left_max, right_max = height[l], height[r]
        total_water = 0
        
        while l < r:
            if left_max <= right_max:
                l += 1
                left_max = max(left_max, height[l])
                total_water +=left_max - height[l] # delta >= 0 because we apply max() before
            else:
                r -= 1
                right_max = max(right_max, height[r])
                total_water +=right_max - height[r]
        return total_water
        
        
        
