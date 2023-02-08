# https://leetcode.com/problems/longest-palindrome/

# General idea:
#Count and take:
# * all even numbers + 
# * all add numbers - 1 + 
# * any lefted letter to the center
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count all elements in string
        count_dict = {}
        for symbol in s:
            count_dict[symbol] = count_dict.get(symbol, 0) + 1

        meet_odd = False # to take first odd subsequence and use as center part
        max_palindrome_size = 0
        print(count_dict)
        for symbol in count_dict:
            if count_dict[symbol] % 2 == 0:
                max_palindrome_size += count_dict[symbol]
            elif not meet_odd: 
                meet_odd = True
                max_palindrome_size += count_dict[symbol]
            else: # take max even amount from add
                max_palindrome_size += count_dict[symbol] - 1
        return max_palindrome_size