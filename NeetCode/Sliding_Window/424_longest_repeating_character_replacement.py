# https://leetcode.com/problems/longest-repeating-character-replacement


# My solution. 
# O(n^2) in time complexity because of max(arr)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        arr = [0] * 26
        max_length = 0
        for r in range(len(s)):
            arr_idx = ord(s[r]) - ord('A')
            arr[arr_idx] += 1
            
            # increase max_length if we meet cindition
            if (r - l + 1) - max(arr) <= k:
                max_length = max(max_length, (r - l + 1))
            # truncate substring from the left, until we meet condition again
            else:
                while (r - l + 1) - max(arr) > k and l < r:
                    arr_idx = ord(s[l]) - ord('A')
                    arr[arr_idx] -= 1
                    l += 1
        return max_length
    
# O(n) in time complexity because of caching
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        l = 0
        max_freq = 0
        max_substr_len = 0
        for r in range(len(s)):
            # update max based on previously added char
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            max_freq = max(freq_map[s[r]], max_freq)

            # Truncate string
            # BTW, we can replace `while`` by `if`
            # Thus we will penalize (r - l + 1) by one, which will be enough
            while (r - l + 1) - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1

            max_substr_len = max(max_substr_len, (r - l + 1))
        return max_substr_len