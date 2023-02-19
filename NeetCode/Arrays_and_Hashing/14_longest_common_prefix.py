# https://leetcode.com/problems/longest-common-prefix/

from typing import List

# My approach - with string slicing
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        for word in strs[1:]:
            while prefix and prefix != word[:len(prefix)]:
                prefix = prefix[:-1]
        return prefix

# Neetcode approach - more memory effective
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for idx in range(len(strs[0])):
            for s in strs:
                # if we will jump out of bounds or find difference in prefix
                if idx == len(s) or s[idx] != strs[0][idx]:
                    return res
            res += strs[0][idx]
        # in case of equal or only one string
        return res