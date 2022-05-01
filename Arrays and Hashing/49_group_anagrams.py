
#https://leetcode.com/problems/group-anagrams/ 
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ## Need sorting to keep the same keys order for every anagram 
        # def get_anagram_state(s):
        #     anagram_dict = {}
        #     for item in s:
        #         if item not in anagram_dict:
        #             anagram_dict[item] = s.count(item)
        #     ordered_dict = {k: v for k, v in sorted(list(anagram_dict.items()))}
        #     return str(ordered_dict)
        
        def get_anagram_state(s):
            counter = [0] * 26 # a...z
            for letter in s:
                counter[ord(letter) - ord('a')] += 1
            return str(counter)
        
        result_hash = dict()
        for word in strs:
            anagram_dict = str(get_anagram_state(word))
            if anagram_dict not in result_hash:
                result_hash[anagram_dict] = [word]
            else:
                result_hash[anagram_dict].append(word)
        return result_hash.values()
