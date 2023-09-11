# https://leetcode.com/problems/longest-palindromic-substring/

# Time complexity: O(n^2)
# Memory complexity: O(n)
# Main idea - find palindrom by substring expanding for every odd/even starting position
# babad -> b, |bab|, b|aba|d, bad, d; For odd palindroms l==r
# babad -> ba, baba, abad, ad; For even palindroms l==r - 1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        max_palindrom = ""
        for i in range(len(s)):
            odd_palindrom = self.get_max_palindrom(s, i, i)
            even_palindrom = self.get_max_palindrom(s, i, i+1)
            max_palindrom = max([max_palindrom, odd_palindrom, even_palindrom], key = lambda x: len(x))
        return max_palindrom

    def get_max_palindrom(self, s: str, l: int, r:int):
        """
        Helper function that find max palindrom based on expanded window
        Odd palindrom case: l == r - 
        Even palindrom case: l == r - 1 
        """
        res = ""
        reslen = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    reslen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res