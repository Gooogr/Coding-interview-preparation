# https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_list = [0] * 26
        for l in magazine:
            mag_list[self.get_idx(l)] += 1
        for l in ransomNote:
            idx = self.get_idx(l)
            mag_list[idx] -= 1
            if mag_list[idx] < 0:
                return False
        return True
    
    def get_idx(self, l:str):
        return ord(l) - ord("a")