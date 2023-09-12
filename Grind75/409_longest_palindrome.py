# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_dict = {}
        total = 0
        have_odd = False

        for l in s:
            count_dict[l] = count_dict.get(l, 0) + 1

        for k, v in count_dict.items():
            if v % 2 == 0:
                total += v
                count_dict[k] = 0
            else:
                total += v - 1
                have_odd = True
                count_dict[k] = 1

        if have_odd:
            total += 1
        return total