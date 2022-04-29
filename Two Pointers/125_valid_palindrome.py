# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l_idx = 0
        r_idx = len(s) - 1
        while l_idx < r_idx:
            if not s[l_idx].isalnum():
                l_idx += 1
            elif not s[r_idx].isalnum():
                r_idx -= 1
            elif s[l_idx].lower() != s[r_idx].lower():
                return False
            else:
                l_idx += 1
                r_idx -= 1
        return True

# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         s = s.lower()
#         clean_symbols = []
#
#         for idx in range(len(s)):
#             if s[idx].isalnum():
#                 clean_symbols.append(s[idx])
#         s = ''.join(clean_symbols)
#         n = len(s)
#
#         for idx in range(n//2):
#             left_element = s[idx]
#             right_element = s[n-idx-1]
#             if left_element != right_element:
#                 return False
#         return True
