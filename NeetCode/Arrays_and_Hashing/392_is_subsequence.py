# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Edgecase for empty substing
        if len(s) == 0:
            return True
        
        # Check if we meet every substring element in correct order
        substring_idx = 0
        for letter in t:
            if s[substring_idx] == letter:
                substring_idx += 1
            if len(s) == substring_idx:
                return True
        return False