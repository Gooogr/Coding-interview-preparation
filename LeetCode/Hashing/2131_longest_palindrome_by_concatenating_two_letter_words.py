# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_freq = dict() # <- replace by freq_dict for repeated values
        max_len = 0
        # find symmetry subparts
        for word in words:
            inverted_word = word[::-1]
            if inverted_word in word_freq:
                max_len += 2 * len(word)
                word_freq[inverted_word] -= 1
                # edgecase when ['aa', 'aa', 'aa', 'aa']
                # prevent word_freq go below zero
                if word_freq[inverted_word] == 0:
                    del word_freq[inverted_word]
            else:
                word_freq[word] = word_freq.get(word, 0) + 1
        # find max central part
        max_central_part = 0
        for word in word_freq:
            if word_freq[word] != 0 and self.is_palindrome(word):
                max_central_part = max(max_central_part, len(word))
        return max_len + max_central_part

    def is_palindrome(self, s:str):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True