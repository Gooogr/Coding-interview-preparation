
#https://leetcode.com/problems/group-anagrams/ 
# My initial approach. Far from optimal :)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        def get_anagram_dict(s):
            anagram_dict = {}
            for item in s:
                if item not in anagram_dict:
                    anagram_dict[item] = s.count(item)
            ordered_dict = {k: v for k, v in sorted(list(anagram_dict.items()))}
            return ordered_dict
        
        result_hash = dict()
        for word in strs:
            anagram_dict = str(get_anagram_dict(word))
            if anagram_dict not in result_hash:
                result_hash[anagram_dict] = [word]
            else:
                result_hash[anagram_dict].append(word)
        return result_hash.values()
