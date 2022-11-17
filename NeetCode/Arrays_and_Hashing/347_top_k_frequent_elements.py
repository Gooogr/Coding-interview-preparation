#https://leetcode.com/problems/top-k-frequent-elements/
# Naive approach with complexity O(n*Log(n)) - full sort at the end
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        freq_hash = dict()
        for num in nums:
            if num not in freq_hash:
                freq_hash[num] = 1
            else:
                freq_hash[num] += 1
        return [k for k, v in sorted(freq_hash.items(), key=lambda x: x[1], reverse=True)][:k]

# Better approach - use max heap and extract only necessary elements amount
# Complexity: O(k*log(n))

# Even better - sublists where idx = value frequency
# Complexity: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
            
        # Find frequnecy for every unique value
        freq_hash = dict()
        for num in nums:
            freq_hash[num] = freq_hash.get(num, 0) + 1
            
        # Put values in sublists based on their frequency (sublist idx = frequency)
        # We need nums + 1 baskets, becasue in worst case (all values are the same)
        # freq = len(nums) + 1 and all other buskest would be empty.
        freq_list = [[] for _ in range(len(nums) + 1)]
        print(freq_list)
        for value, freq in freq_hash.items():
            freq_list[freq].append(value)
            
        # Extract K most frequent elements
        result = []
        for sublist in freq_list[::-1]:
            for value in sublist:
                result.append(value)
                if len(result) == k:
                    return result
            


