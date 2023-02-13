# https://leetcode.com/problems/word-break/

from typing import List

# Naive recursive solution - TL error
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def can_break(s, wordDict, start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start : end] in wordDict and can_break(s, wordDict, end):
                    return True
            return False  
        return can_break(s, set(wordDict), 0)