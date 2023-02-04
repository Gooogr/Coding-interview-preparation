# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List

## Additional memory
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         result = []
#         subsum = 0
#         for item in nums:
#             result.append(item + subsum)
#             subsum += item
#         return result
            
## Inplace
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):
            if idx > 0:
                nums[idx] = nums[idx] + nums[idx - 1]
        return nums