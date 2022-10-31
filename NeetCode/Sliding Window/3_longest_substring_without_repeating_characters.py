# https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        subset = set()
        result = 0
        l = 0
        
        for r in range(len(s)):
            # If truncate set from the left, until we eliminate all duplicates in substring
            while s[r] in subset:
                subset.remove(s[l])
                l += 1
            # Now we can safely add new element
            subset.add(s[r])
            # Check elemnts amount in our substing. The same amount if hash 
            result = max(result, len(subset))
        return result
