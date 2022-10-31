# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 1
        
        # In case of empty list
        if len(nums) == 0:
            return 0
        
        for value in nums:
            # check if value is the beggining of the sequence
            if (value - 1) not in num_set:
                current_length = 1
                # Count how many elemnts we have in this sequence
                while (value + current_length) in num_set:
                    current_length += 1
                    max_length = max(max_length, current_length)
        return max_length
