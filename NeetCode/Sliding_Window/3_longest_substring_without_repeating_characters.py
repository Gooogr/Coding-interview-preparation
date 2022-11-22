# https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        string_char = set()
        for r in range(len(s)):
            # remove repeated letters from hash from the left side of substring
            # make step with left pointer
            while s[r] in string_char:
                string_char.remove(s[l])
                l += 1
            # add new unique letter to the hash from right side of substring
            string_char.add(s[r])
            max_len = max(max_len, r - l  + 1)
        return max_len
