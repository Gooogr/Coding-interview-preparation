# https://leetcode.com/problems/find-all-anagrams-in-a-string

from typing import List

# Dynamically update dict of sliding substring
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start_idx = 0
        p_map = {}
        s_map = {}
        result = []
        # create p map (count dict)
        for char in p:
            p_map[char] = p_map.get(char, 0) + 1
        # iterate through s string
        for idx, char in enumerate(s):
            s_map[char] = s_map.get(char, 0) + 1
            # start slising when we have enough data
            if idx >= len(p) - 1:
                if s_map == p_map:
                    result.append(start_idx)
                # update s_map
                out_symbol = s[start_idx]
                s_map[out_symbol] -= 1
                if s_map[out_symbol] == 0:
                    del s_map[out_symbol]
                start_idx +=1
        return result

# Naive approach - TL error
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def get_anagram_code(str1):
            _list = [0] * 26
            for idx in range(len(str1)):
                list_idx = ord(str1[idx]) - ord('a')
                _list[list_idx] += 1
            return _list

        result = []
        p_code = get_anagram_code(p)
        for idx in range(len(s) - len(p) + 1):
            sp_code = get_anagram_code(s[idx:idx + len(p)])
            if p_code == sp_code: 
                result.append(idx)
        return result