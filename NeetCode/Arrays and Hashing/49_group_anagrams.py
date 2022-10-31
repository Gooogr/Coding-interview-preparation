#https://leetcode.com/problems/group-anagrams/ 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def get_anagram_state(word: str) -> list[int]:
            state = [0] * 26 #a..z
            for letter in word:
                state_idx = ord(letter) - ord('a')
                state[state_idx] += 1
            return str(state)
        
        anagrams_hash = dict()
        for word in strs:
            state = get_anagram_state(word)
            if state not in anagrams_hash:
                anagrams_hash[state] = [word]
            else:
                anagrams_hash[state].append(word)
        return anagrams_hash.values()

# With default dict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
	anagrams_hash = collections.defaultdict(list)
	for word in strs:
	    state = [0] * 26
	    for letter in word:
	        state[ord(letter) - ord('a')] += 1
	    anagrams_hash[str(state)].append(word)
	return anagrams_hash.values()


