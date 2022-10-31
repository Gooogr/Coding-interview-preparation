# https://leetcode.com/problems/valid-anagram/
class Solution:
    # Complexity O(N), Memory O(N)
    # Can be solved with memory O(1) but complexity O(n*logn) by
    # return sorted(s) == sorted(t)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = {item: 0 for item in s}
        t_count = {item: 0 for item in t}
        for item in s:
            s_count[item] += 1
        for item in t:
            t_count[item] += 1
        return s_count == t_count
