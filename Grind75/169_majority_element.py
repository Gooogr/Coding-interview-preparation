# https://leetcode.com/problems/majority-element

from typing import List

# Boyer–Moore majority vote algorithm with O(1) memory
# We was garanteed that we have majority element, so can do only one pass!
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = None
        count = 0

        for num in nums:
            if count == 0:
                major = num
                count = 1
            else:
                if num == major:
                    count += 1
                else:
                    count -= 1
        return major
