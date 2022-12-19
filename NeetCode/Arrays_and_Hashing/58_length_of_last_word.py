# https://leetcode.com/problems/length-of-last-word/

# With python magic
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        return len(arr[-1])

# Brutal while loops
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0
        # find last non-space element in string
        while s[i] == ' ':
            i -= 1
        # count all symbols until string end or next space
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length