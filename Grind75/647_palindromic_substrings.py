# https://leetcode.com/problems/palindromic-substrings/

# Time complexity: O(n^2)
# Memory complexity: O(1)
# Similar to Leetcode 5 (longest palindromic substring)
class Solution:
    def countSubstrings(self, s: str) -> int:
        total_amount = 0
        for i in range(len(s)):
            total_amount += self.count_palindroms(s, i, i)
            total_amount += self.count_palindroms(s, i, i+1)
        return total_amount

    def count_palindroms(self, s: str, l: int, r: int):
        pal_counter = 0
        while l >=0 and  r < len(s) and s[l] == s[r]:
            pal_counter += 1
            l -= 1
            r += 1
        return pal_counter