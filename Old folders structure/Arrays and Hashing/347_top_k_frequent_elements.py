#https://leetcode.com/problems/top-k-frequent-elements/
# Naive approach with sorted dict keys
# Complexity: O(n**2)
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
# Complexity: O(k*log(n))

# Even better - bucket sort approach
# Complexity: O(n)

# General idea: use list where:
# indecis - times of element occurence
# values - list of elements with the same occurence
# Default length of this array equal to len(nums), because in the worst case all 
# elements are unique.

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = dict()
        freq = [[] for _ in range(len(nums) + 1)]
        
        # Count element frequency occurenece and save in hashmap
        for number in nums:
            count[number] = count.get(number, 0) + 1
            
        # Place every pair in list.
        # Structure: index - frequency, values - corresponded lists of values
        for number, freq_idx in count.items():
            freq[freq_idx].append(number)
        
        # extract target amount of numbers from comprehended list
        result = []
        for idx in range(len(freq) -1, 0, -1):
            for number in freq[idx]:
                result.append(number)
                if len(result) == k:
                    return result


