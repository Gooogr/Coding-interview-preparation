# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_cache = set()
        max_len = 0
        l = 0
        if len(s) < 2:
            return len(s)
        for r in range(len(s)):
            while s[r] in letter_cache:
                letter_cache.remove(s[l])
                l += 1
            letter_cache.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len