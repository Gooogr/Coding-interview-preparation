# https://leetcode.com/problems/valid-anagram/
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        # Valid anagram == Equal amount of elements
        s_dict = dict()
        t_dict = dict()
        
        for item in set(s):
            s_dict[item] = s.count(item)
            t_dict[item] = t.count(item)
            
        return s_dict == t_dict
