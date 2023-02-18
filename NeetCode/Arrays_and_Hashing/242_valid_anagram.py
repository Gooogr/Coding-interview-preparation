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
    
# Or more memory efficient, because 
# list need less space than dict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        def get_str_code(s: str):
            arr = [0] * 26
            for char in s:
                idx = ord(char) - ord('a')
                arr[idx] += 1
            return arr

        return get_str_code(s) == get_str_code(t)
