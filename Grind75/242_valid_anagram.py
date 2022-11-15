# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash = {}
        t_hash = {}
        for item in s:
            s_hash[item] = s_hash.get(item, 0) + 1
        for item in t:
            t_hash[item] = t_hash.get(item, 0) + 1
        return s_hash == t_hash
        