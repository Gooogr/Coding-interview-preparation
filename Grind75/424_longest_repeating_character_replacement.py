# https://leetcode.com/problems/longest-repeating-character-replacement/

# Time complexity: O(26*n) -> O(n)
# Memory complexity: O(26)
# Two pointers with condition, that we need less than 
# K replaces by the most popular symbol in our substring
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dict = {}
        result = 0
        l = 0
        for r in range(len(s)):
            count_dict[s[r]] = count_dict.get(s[r], 0) + 1
            if (r - l + 1) - max(count_dict.values()) > k:
                count_dict[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result