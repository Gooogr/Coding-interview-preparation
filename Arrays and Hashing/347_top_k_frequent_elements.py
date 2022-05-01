#https://leetcode.com/problems/top-k-frequent-elements/
# Naive approach with sorted dict keys
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_count = dict()
        for item in set(nums):
            dict_count[item] = nums.count(item)
        sorted_keys = [key for key, _ in sorted(dict_count.items(), 
                                                key = lambda x: x[1],
                                                reverse = True)]
        return sorted_keys[:k]

# Better approach - use max heap and extract only necessary elements amount
