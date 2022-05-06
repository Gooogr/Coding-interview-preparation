# https://www.lintcode.com/problem/659/
# https://leetcode.com/problems/encode-and-decode-strings/ (premium only)

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        result = '_|_'.join(item for item in strs) # becasue _|_ just works fine
        return result

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        return str.split('_|_')
